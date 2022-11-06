from collections import deque

map = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]

visited = [[0] * len(map[i]) for i in range(len(map))]

def bfs(i, j, map, visited):
    
    N, M = len(map) - 1, len(map[0]) - 1
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque()
    
    q.append((i, j))
    visited[i][j] = 1
    map[i][j] = 1
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in direct:
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr <= N and 0 <= nc <= M and map[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                map[nr][nc] = 1
                q.append((nr, nc))
    
    return map

answer = 0

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            bfs(i, j, map, visited)
            answer += 1

answer
