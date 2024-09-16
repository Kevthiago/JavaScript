from collections import deque

def bfs_paths(maze, start, end_value):
    """Encontra todos os caminhos do início ao valor final usando BFS."""
    queue = deque([(start, [start], 0)])  # (posição atual, caminho, número de paredes)
    visited = set()
    all_paths = []
    visited.add(start)
    
    while queue:
        (x, y), path, walls = queue.popleft()
        
        if maze[x][y] == end_value:
            all_paths.append((path, walls))
            if len(all_paths) >= 10:  # Para limitar a quantidade de caminhos encontrados
                break
            continue
        
        for (nx, ny) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if (0 <= nx < 42 and 0 <= ny < 42 and (nx, ny) not in visited):
                new_walls = walls + (1 if maze[nx][ny] == 1 else 0)
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)], new_walls))
    
    return all_paths

def dfs_paths(maze, start, end_value):
    """Encontra todos os caminhos do início ao valor final usando DFS."""
    stack = [(start, [start], 0)]  # (posição atual, caminho, número de paredes)
    visited = set()
    all_paths = []
    
    while stack:
        (x, y), path, walls = stack.pop()
        
        if maze[x][y] == end_value:
            all_paths.append((path, walls))
            if len(all_paths) >= 10:  # Para limitar a quantidade de caminhos encontrados
                break
            continue
        
        visited.add((x, y))
        
        for (nx, ny) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if (0 <= nx < 42 and 0 <= ny < 42 and (nx, ny) not in visited):
                new_walls = walls + (1 if maze[nx][ny] == 1 else 0)
                stack.append(((nx, ny), path + [(nx, ny)], new_walls))
    
    return all_paths

def find_best_paths(maze):
    """Encontra os 3 melhores caminhos do início ao final usando BFS e DFS."""
    start = (1, 0)
    end_value = 42

    # Encontra caminhos usando BFS
    bfs_all_paths = bfs_paths(maze, start, end_value)
    
    # Encontra caminhos usando DFS
    dfs_all_paths = dfs_paths(maze, start, end_value)

    # Combina todos os caminhos encontrados por BFS e DFS
    all_paths = bfs_all_paths + dfs_all_paths
    
    if not all_paths:
        return []

    # Ordena caminhos pelo comprimento e pelo número de paredes (menos paredes é melhor)
    sorted_paths = sorted(all_paths, key=lambda x: (len(x[0]), x[1]))
    
    # Pega os 3 melhores caminhos
    best_paths = [path for path, _ in sorted_paths[:3]]
    
    return best_paths

if __name__ == "__main__":
    # Exemplo de matriz 42x42, substitua com o labirinto real
    maze = [[0]*42 for _ in range(42)]
    
    # Define o início e o fim
    maze[1][0] = 0  # Posição de início
    maze[41][41] = 42  # Posição de fim
    
    # Adiciona algumas paredes para criar um labirinto
    # Adicione as paredes manualmente conforme o labirinto real que você tem
    # Exemplo simples de adicionar paredes (isto deve ser substituído pelo labirinto real)
    for i in range(42):
        if i % 2 == 0:
            maze[i][i % 42] = 1
    
    best_paths = find_best_paths(maze)
    
    # Imprime os 3 melhores caminhos encontrados no formato esperado
    if best_paths:
        formatted_paths = [[(x, y) for (x, y) in path] for path in best_paths]
        print(formatted_paths)  # Exemplo de saída: [[(1, 1), ..., (40, 41)], [(1, 1), ..., (40, 41)], [(1, 1), ..., (40, 41)]]
    else:
        print("Nenhum caminho válido encontrado.")
