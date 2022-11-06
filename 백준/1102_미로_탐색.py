import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

Map = []
for _ in range(N):
    Map.append(list(map(int, input().rstrip())))

visited = [[0] * len(Map[0]) for _ in range(len(Map))]
q = deque()

q.append((0, 0))
visited[0][0] = 1

direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while q:
    
    r, c = q.popleft()
    
    for rd, cd in direct:
        
        nr = r + rd
        nc = c + cd
        
        if 0 <= nr < N and 0 <= nc < M:
            if Map[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

print(visited[N - 1][M - 1])
