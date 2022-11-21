from collections import deque

# BFS
def bfs(graph, N, r, c, color, visited, cnt):
    q = deque()
    
    direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    q.append((r, c))
    visited[r][c] = 1
    
    while q:
        r, c = q.popleft()
        for dr, dc in direct:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == color and visited[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
    
    return cnt + 1

N = int(input())

# 정상인 구역 

graph = []
for _ in range(N):
    row = []
    s = input()
    for c in s:
        row.append(c)
    graph.append(row)
visited = [[0] * N for _ in range(N)]
colors = ['R', 'G', 'B']
cnt = 0

for r in range(N):
    for c in range(N):
        for color in colors:
            if graph[r][c] == color and visited[r][c] == 0:
                cnt = bfs(graph, N, r, c, color, visited, cnt)

# 적록색약 구역

graph2 = graph.copy()
visited2 = [[0] * N for _ in range(N)]
colors2 = ['R', 'B']
cnt2 = 0

for r in range(N):
    for c in range(N):
        if graph2[r][c] == 'G':
            graph2[r][c] = 'R'

for r in range(N):
    for c in range(N):
        for color2 in colors2:
            if graph2[r][c] == color2 and visited2[r][c] == 0:
                cnt2 = bfs(graph2, N, r, c, color2, visited2, cnt2)

print(cnt, cnt2)
