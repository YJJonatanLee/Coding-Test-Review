
N = int(input())

people = []
for _ in range(N):
    people.append(tuple(map(int, input().split())))

ranks = []
for w, h in people:
    rank = 1
    for w1, h1 in people:
        if w < w1 and h < h1:
            rank += 1
    ranks.append(rank)
    
print(*ranks)
