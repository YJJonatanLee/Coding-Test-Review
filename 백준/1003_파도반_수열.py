n = 12

memo = [0] * (n + 1)

memo[1], memo[2], memo[3] = 1, 1, 1

for i in range(4, n + 1):
    memo[i] = memo[i - 2] + memo[i - 3]
    
print(memo[n])
