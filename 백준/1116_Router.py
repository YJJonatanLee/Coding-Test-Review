from collections import deque

N = 5
packets = deque([1, 2, 0, 3, 4, 0, 5, 6, 0, 0, -1])

router = deque()

while packets[0] != -1:
    p = packets.popleft()
    if p != 0:
        if len(router) >= N:
            continue
        else:
            router.append(p)
    else:
        router.popleft()

print(*router)
