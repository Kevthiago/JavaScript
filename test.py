import websocket
from collections import deque

def is_visible(grid, guard_pos, direction):
    """Verifica se o guarda é visível a partir da posição dada, com base na direção que ele está olhando."""
    x, y = guard_pos
    if direction == '^':
        for i in range(x - 1, -1, -1):
            if grid[i][y] == '🏠':
                break
            if grid[i][y] == '🥷':
                return True
        return False
    elif direction == 'v':
        for i in range(x + 1, len(grid)):
            if grid[i][y] == '🏠':
                break
            if grid[i][y] == '🥷':
                return True
        return False
    elif direction == '<':
        for j in range(y - 1, -1, -1):
            if grid[x][j] == '🏠':
                break
            if grid[x][j] == '🥷':
                return True
        return False
    elif direction == '>':
        for j in range(y + 1, len(grid[0])):
            if grid[x][j] == '🏠':
                break
            if grid[x][j] == '🥷':
                return True
        return False
    return False

def bfs_path_exists(map_matrix, start, end):
    """Verifica se há um caminho do início até o fim usando BFS."""
    rows = len(map_matrix)
    cols = len(map_matrix[0])
    queue = deque([start])
    visited = set()
    visited.add(start)

    while queue:
        current = queue.popleft()
        if current == end:
            return True
        
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and map_matrix[nx][ny] in (' ', '💻'):
                visited.add((nx, ny))
                queue.append((nx, ny))
    
    return False

def parse_map(map_str):
    """Parse o mapa da string."""
    lines = map_str.strip().split('\n')
    map_matrix = [list(line) for line in lines]

    # Localize Loid, terminal e guardas
    loid_pos = None
    terminal_pos = None
    guards = []

    for i, row in enumerate(map_matrix):
        for j, cell in enumerate(row):
            if cell == '🥷':
                loid_pos = (i, j)
            elif cell == '💻':
                terminal_pos = (i, j)
            elif cell in '^v<>':
                guards.append(((i, j), cell))

    return map_matrix, loid_pos, terminal_pos, guards

def mark_invisible_areas(map_matrix, guard_pos, direction):
    """Marca as áreas visíveis dos guardas como obstáculos."""
    x, y = guard_pos
    if direction == '^':
        for i in range(x - 1, -1, -1):
            if map_matrix[i][y] in ('🥷', '💻', '🏠'):
                break
            map_matrix[i][y] = '🏠'
    elif direction == 'v':
        for i in range(x + 1, len(map_matrix)):
            if map_matrix[i][y] in ('🥷', '💻', '🏠'):
                break
            map_matrix[i][y] = '🏠'
    elif direction == '<':
        for j in range(y - 1, -1, -1):
            if map_matrix[x][j] in ('🥷', '💻', '🏠'):
                break
            map_matrix[x][j] = '🏠'
    elif direction == '>':
        for j in range(y + 1, len(map_matrix[0])):
            if map_matrix[x][j] in ('🥷', '💻', '🏠'):
                break
            map_matrix[x][j] = '🏠'

def decide_action(map_str):
    """Decide se é seguro avançar ou não."""
    map_matrix, loid_pos, terminal_pos, guards = parse_map(map_str)

    if terminal_pos is None or loid_pos is None:
        return "Espere!"

    # Marca as áreas visíveis pelos guardas como obstáculos
    for guard_pos, direction in guards:
        mark_invisible_areas(map_matrix, guard_pos, direction)

    # Verifica se há um caminho seguro do Loid ao terminal
    action = "Vai!" if bfs_path_exists(map_matrix, loid_pos, terminal_pos) else "Espere!"

    return action

# URL da API da CTF
base_url = "wss://ctf-challenges.devops.hotmart.com/echo"  # Substitua com a URL real

def on_message(ws, message):
    print(f"Mensagem recebida: {message}")

    # Processa apenas mensagens relevantes
    if "[*] Mapa:" in message:
        map_str = message.split("[*] Mapa:")[1].strip()
        action = decide_action(map_str)
        print(f"Enviando: {action}")
        ws.send(action)
    elif "[*] Sucesso!" in message:
        print("Mensagem processada:", message)
    elif "[*] Errou!" in message:
        print("Erro na resposta")
    elif "Código Final:" in message:
        code = message.split("Código Final:")[1].strip()
        print(f"Código final recebido: {code}")

def on_error(ws, error):
    print("Erro:", error)

def on_close(ws, close_status_code, close_msg):
    print("Conexão fechada:", close_status_code, close_msg)

def on_open(ws):
    print("Conexão aberta")
    # Envia o comando para iniciar o desafio
    ws.send("start spy")

# Executa a conexão WebSocket
ws = websocket.WebSocketApp(base_url,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)

ws.run_forever()
