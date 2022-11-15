from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

c_comb = combinations(cards, 3)

c_list = []
for c in c_comb:
    if sum(c) <= M:
        c_list.append(sum(c))

print(max(c_list))
