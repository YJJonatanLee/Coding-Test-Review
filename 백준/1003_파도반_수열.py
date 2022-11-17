T = int(input())

for _ in range(T):
    n = int(input())
    
    memo = [0] * 100

    memo[0], memo[1], memo[2] = 1, 1, 1

    for i in range(3, n):
        memo[i] = memo[i - 2] + memo[i - 3]
        
    print(memo[n - 1])
