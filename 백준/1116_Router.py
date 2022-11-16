from collections import deque

N = int(input())
buffer = deque()

while True:
    packet = int(input())
    if packet == -1:
        break
    if packet != 0:
        if len(buffer) >= N:
            continue
        else:
            buffer.append(packet)
    else:
        buffer.popleft()

if buffer:
    print(*buffer)
else:
    print('empty')
