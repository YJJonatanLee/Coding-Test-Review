from collections import deque

N = 7
K = 3

q = deque([i for i in range(1, N + 1)])
answer = []
q
answer

while q:
    for _ in range(K - 1):
        a = q.popleft()
        q.append(a)
    b = q.popleft()
    answer.append(b)
    
q
answer
