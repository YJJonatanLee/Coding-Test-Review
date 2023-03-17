from collections import deque

N, K = map(int, input().split())

def bfs(N, K):
    
    q = deque()
    visited = [0] * 100001

    cnt = 0
    q.append((cnt, N))
    visited[N] = 1
    
    if N == K:
        return cnt

    while q:
        cnt, num = q.popleft()
        for n_num in (num + 1, num - 1, num * 2):
            if 0 <= n_num <= 100000 and visited[n_num] == 0:
                if n_num == K:
                    return cnt + 1
                else:
                    q.append((cnt + 1, n_num))
                    visited[n_num] = 1
                
answer = bfs(N, K)

print(answer)
