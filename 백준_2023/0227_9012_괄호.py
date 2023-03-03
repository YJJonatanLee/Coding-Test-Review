N = int(input())

for _ in range(N):
    s = str(input())
    
    stack = []

    for b in s:
        if b == '(':
            stack.append(b)
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')
