from collections import defaultdict

N = int(input())
N_nums = list(map(int, input().split()))

M = int(input())
M_nums = list(map(int, input().split()))

N_hash = defaultdict(int)
for num in N_nums:
    N_hash[num] += 1

answer = []
for num in M_nums:
    answer.append(N_hash[num])
    
print(*answer)
