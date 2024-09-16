import websocket
import json

def solve_hanoi(n, start='A', end='C', temp='B'):
    moves = []
    def hanoi(n, start, end, temp):
        if n > 0:
            hanoi(n - 1, start, temp, end)
            moves.append((start, end))
            hanoi(n - 1, temp, end, start)
    hanoi(n, start, end, temp)
    return moves

def format_moves(moves):
    return str(moves).replace(" ", "")  # Formata a lista de movimentos sem espaços adicionais

def on_message(ws, message):
    print(f"Mensagem recebida: {message}")

    if "Príncipes:" in message:
        try:
            príncipes = int(message.split("Príncipes:")[1].split()[0].strip("[]"))
            movimentos_minimos = int(message.split("Movimentos Mínimos Necessários:")[1].split()[0].strip("[]"))
            
            # Calcula os movimentos para a Torre de Hanói
            resposta = solve_hanoi(príncipes)
            response_str = format_moves(resposta)
            print(f"Enviando resposta: {response_str}")
            ws.send(response_str)
        except ValueError as e:
            print(f"Erro ao processar a mensagem: {e}")

    elif "Entrada inválida" in message:
        print("Entrada inválida. Enviando novamente a resposta formatada.")
        try:
            resposta = solve_hanoi(príncipes)
            response_str = format_moves(resposta)
            ws.send(response_str)
        except:
            print("Erro ao enviar a resposta.")

    elif "[*] Stage:" in message:
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
    ws.send("start towerofhanoi")  # Comando para iniciar o desafio

# URL da API da CTF
base_url = "wss://ctf-challenges.devops.hotmart.com/echo"  # Substitua com a URL real

# Executa a conexão WebSocket
ws = websocket.WebSocketApp(base_url,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()
