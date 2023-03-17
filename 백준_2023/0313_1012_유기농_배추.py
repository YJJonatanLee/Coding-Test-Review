from collections import deque

def bfs(graph, r, c):
    
    N = len(graph)
    M = len(graph[0])
    
    direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    q = deque()
    
    q.append((r, c))
    graph[r][c] = 0
    
    while q:
        
        r, c = q.popleft()
        
        for rd, cd in direct:
            
            nr = r + rd
            nc = c + cd
            
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 1:
                    graph[nr][nc] = 0
                    q.append((nr, nc))
                    
    return cnt

T = int(input())

for _ in range(T):
    
    cnt = 0
    
    M, N, K = list(map(int, input().split()))
    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        c, r = list(map(int, input().split()))
        graph[r][c] = 1

    for r in range(N):
        for c in range(M):
            if graph[r][c] == 1:
                bfs(graph, r, c)
                cnt += 1

    print(cnt)
