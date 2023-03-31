T = int(input())

for _ in range(T):
    
    k = int(input())
    n = int(input())

    Map = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        Map[0][i] = i

    for r in range(1, k + 1):
        for c in range(1, n + 1):
            Map[r][c] = sum(Map[r-1][1:c+1])
            
    print(Map[k][n])
