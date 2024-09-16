import websocket
import json

def kadane_algorithm(arr):
    # Inicializa variáveis
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    # Itera sobre o array a partir do segundo elemento
    for x in arr[1:]:
        # Atualiza o max_ending_here
        max_ending_here = max(x, max_ending_here + x)
        # Atualiza o max_so_far
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

def on_message(ws, message):
    print(f"Mensagem recebida: {message}")

    if "[*] Array:" in message:
        try:
            # Extraí o array da mensagem
            array_str = message.split("[*] Array:")[1].strip()
            
            # Remove colchetes e espaços extras
            array_str = array_str.strip('[]').replace(" ", "")
            
            # Converte a string para uma lista de inteiros
            colina = list(map(int, array_str.split(',')))
            
            # Exibe o array recebido
            print(f"Array recebido: {colina}")
            
            # Resolve o problema usando o Algoritmo de Kadane
            result = kadane_algorithm(colina)
            
            # Envia a resposta como um número inteiro
            response = str(result)  # Envia apenas o número
            response = response.strip()  # Remove possíveis espaços extras
            
            # Envia a resposta e exibe no terminal
            ws.send(response)
            print(f"Resposta enviada: {response}")
        except ValueError:
            error_response = "Resposta: Erro"
            ws.send(error_response)
            print(f"Resposta enviada: {error_response}")

def on_error(ws, error):
    print("Erro:", error)

def on_close(ws, close_status_code, close_msg):
    print("Conexão fechada:", close_status_code, close_msg)

def on_open(ws):
    start_command = "start lost_treasure"
    ws.send(start_command)
    print(f"Comando enviado: {start_command}")

# URL da API da CTF
base_url = "wss://ctf-challenges.devops.hotmart.com/echo"  # Substitua com a URL real

# Executa a conexão WebSocket
ws = websocket.WebSocketApp(base_url,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()
