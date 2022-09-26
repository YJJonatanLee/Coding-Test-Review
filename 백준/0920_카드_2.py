import sys
from collections import deque

n = int(sys.stdin.readline())
cards = [i for i in range(1,n+1)]
cards_deque = deque(cards)
while len(cards_deque) > 1:
    cards_deque.popleft()
    cards_deque.append(cards_deque.popleft())
print(cards_deque[0])
