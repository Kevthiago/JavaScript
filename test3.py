import websocket
import hashlib
import base64
import codecs

# Variáveis globais para armazenar partes da mensagem
method = None
encoded_text = None
key = None

# Função para calcular hash no formato fornecido
def hashhex(s):
    h = hashlib.new()
    h.update(s)
    return h.hexdigest()

def process_text(method, text, key=None):
    if method == "base64":
        # Decodifica Base64 e retorna o texto decodificado
        return base64.b64decode(text).decode('utf-8')
    elif method == "hex":
        # Converte de hexadecimal para texto
        return bytes.fromhex(text).decode('utf-8')
    elif method == "binary":
        # Remove o prefixo '[+] Encoded: ' e espaços
        binary_str = text[len('[+] Encoded: '):].strip()

        # Converte a string binária em blocos de 8 bits e depois para texto
        binary_values = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
        clear_text = ''.join(ascii_characters)
        # Substitui espaços por '_'
        formatted_text = '_'.join(clear_text.split())
        # Exibe a resposta formatada
        return formatted_text
    elif method == "single_byte_xor":
        # Decodifica Base64, aplica XOR com a chave e retorna o texto decodificado
        decoded_bytes = base64.b64decode(text)
        key = int(key, 16)
        result_bytes = bytearray(b ^ key for b in decoded_bytes)
        return result_bytes.decode('utf-8')
    elif method == "rot-13":
        # Aplica ROT13 para decifrar a mensagem
        return codecs.decode(text, 'rot_13')
    elif method == "caesar":
        # Aplica a cifra de César com um deslocamento opcional
        shift = int(key) if key else 3
        decoded = []
        for char in text:
            if char.isalpha():
                shift_amount = shift if char.islower() else -shift
                decoded_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift_amount) % 26 + ord('a' if char.islower() else 'A'))
                decoded.append(decoded_char)
            else:
                decoded.append(char)
        return ''.join(decoded)
    else:
        # Caso o método não seja reconhecido, retorna o texto como está
        return '_'.join(text.split())

def process_hash(method, text):
    encoded_text = text.encode('utf-8')
    if method == "md5":
        return hashhex(encoded_text)
    elif method == "sha1":
        return hashhex(encoded_text)
    else:
        raise ValueError("Método de hash não suportado")

# Função principal que processa o método
def process_method(method, encoded_text, key=None):
    if method in ["md5", "sha1"]:
        return process_hash(method, encoded_text)
    elif method in ["binary", "base64", "hex", "single_byte_xor", "rot-13", "caesar"]:
        return process_text(method, encoded_text, key)
    else:
        raise ValueError("Método não suportado")

# Função de callback quando a mensagem é recebida
def on_message(ws, message):
    global method, encoded_text, key
    
    print(f"Received: {message}")
    
    # Verifica se a mensagem contém o método, o texto codificado e a chave
    if "[+] Method:" in message:
        method = message.split(": ")[1].strip()
    
    if "[+] Encoded:" in message:
        encoded_text = message.split(": ")[1].strip()
    
    if "[+] Key:" in message:
        key = message.split(": ")[1].strip()

    if method and encoded_text:
        # Processa o texto de acordo com o método
        response = process_method(method, encoded_text, key)
        
        if response:
            # Imprime a resposta no terminal antes de enviar
            print(f"Resposta enviada: {response}")
            ws.send(response)
        else:
            print("Nenhuma resposta gerada para envio.")

        # Reseta as variáveis para o próximo estágio
        method = None
        encoded_text = None
        key = None

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")
    ws.send("start cryptomix")

# Configurando WebSocket
ws = websocket.WebSocketApp("wss://ctf-challenges.devops.hotmart.com/echo",
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

# Inicia a conexão
ws.run_forever()
