import websocket

def find_longest_palindrome(word):
    """Encontra o maior palíndromo na substring de uma palavra."""
    def is_palindrome(s):
        return s == s[::-1]

    n = len(word)
    longest = ""
    for i in range(n):
        for j in range(i + 2, n + 1):
            substring = word[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest

def on_message(ws, message):
    print(f"Mensagem recebida: {message}")

    if "[*] Word:" in message:
        word = message.split("[*] Word:")[1].strip()
        longest_palindrome = find_longest_palindrome(word)
        
        if longest_palindrome and len(longest_palindrome) > 1:
            response = longest_palindrome
        else:
            response = "Sem palindromo"
        
        print(f"Enviando resposta: {response}")
        ws.send(response)

    elif "[*] Stage:" in message:
        # Mensagens sobre o estágio atual, apenas para informação
        print(f"Mensagem recebida: {message}")

    elif "Código Final:" in message:
        code = message.split("Código Final:")[1].strip()
        print(f"Código final recebido: {code}")

    else:
        print(f"Mensagem não processada: {message}")

def on_error(ws, error):
    print("Erro:", error)

def on_close(ws, close_status_code, close_msg):
    print("Conexão fechada:", close_status_code, close_msg)

def on_open(ws):
    print("Conexão aberta")
    ws.send("start palindromo")  # Comando para iniciar o desafio

# URL da API da CTF
base_url = "wss://ctf-challenges.devops.hotmart.com/echo"  # Substitua com a URL real

# Executa a conexão WebSocket
ws = websocket.WebSocketApp(base_url,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()
