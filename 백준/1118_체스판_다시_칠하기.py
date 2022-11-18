
def even_draw_num(a, b, Map):
    
    cnt = 0
    W_even = 0
    B_even = 0

    for r in range(a, a + 8):
        for c in range(b, b + 8):
            if (r + c) % 2 == 0:
                if Map[r][c] == 'W':
                    W_even += 1
                else:
                    B_even += 1

    if W_even < B_even:
        cnt += W_even
        even = 'B'
    else:
        cnt += B_even
        even = 'W'
        
    for r in range(a, a + 8):
        for c in range(b, b + 8):
            if (r + c) % 2 != 0:
                if Map[r][c] == even:
                    cnt += 1
    
    return cnt

def odd_draw_num(a, b, Map):
    
    cnt = 0
    W_odd = 0
    B_odd = 0

    for r in range(a, a + 8):
        for c in range(b, b + 8):
            if (r + c) % 2 != 0:
                if Map[r][c] == 'W':
                    W_odd += 1
                else:
                    B_odd += 1

    if W_odd < B_odd:
        cnt += W_odd
        odd = 'B'
    else:
        cnt += B_odd
        odd = 'W'
        
    for r in range(a, a + 8):
        for c in range(b, b + 8):
            if (r + c) % 2 == 0:
                if Map[r][c] == odd:
                    cnt += 1
    
    return cnt

N, M = map(int, input().split())

Map = []
for _ in range(N):
    row = []
    s = input()
    for c in s:
        row.append(c)
    Map.append(row)

draw_num_list = []

for a in range(0, N - 7):
    for b in range(0, M - 7):
        even_num = even_draw_num(a, b, Map)
        odd_num = odd_draw_num(a, b, Map)
        draw_num_list.append(min(even_num, odd_num))
        
answer = min(draw_num_list)

print(answer)
