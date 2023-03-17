from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))

def bfs(graph, r, c):
    
    q = deque()
    
    q.append((r, c))
    graph[r][c] = 0
    cnt = 1
    
    direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    while q:
        
        r, c = q.popleft()
        
        for rd, cd in direct:
            
            nr = r + rd
            nc = c + cd
            
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == 1:
                    graph[nr][nc] = 0
                    q.append((nr, nc))
                    cnt += 1
    
    return graph, cnt

cnt_list = []

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            graph, cnt = bfs(graph, r, c)
            cnt_list.append(cnt)

print(len(cnt_list))
for cnt in sorted(cnt_list):
    print(cnt)
