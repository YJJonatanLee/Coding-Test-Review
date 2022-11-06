from collections import deque

N = int(input())
M = int(input())

graph = [[] * N for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(N, graph, s):
    visited = [0] * (N + 1)
    q = deque()

    visited[s] = 1
    q.append(graph[s])

    while q:
        nodes = q.popleft()
        for node in nodes:
            if visited[node] == 0:
                q.append(graph[node])
                visited[node] = 1
    
    return visited.count(1) - 1

print(bfs(N, graph, 1))
