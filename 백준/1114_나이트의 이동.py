from collections import deque

def bfs(start_p, end_p, map):
    
    q = deque()
    direct = [(-1, 2), (1, 2), (2, 1), (-2, 1), (-1, -2), (1, -2), (2, -1), (-2, -1)]

    q.append(start_p)
    
    if start_p == end_p:
        return 0
    
    while q:
        r, c = q.popleft()
        for dr, dc in direct:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < map_rc and 0 <= nc < map_rc and map[nr][nc] == 0:
                if (nr, nc) == end_p:
                    map[nr][nc] = map[r][c] + 1
                    return map[nr][nc]
                else:
                    map[nr][nc] = map[r][c] + 1
                    q.append((nr, nc))

T = int(input())

for _ in range(T):

    map_rc = int(input())
    Map = [[0] * map_rc for _ in range(map_rc)]
    
    r, c = map(int, input().split())
    start_p = (r, c)
    
    r_end, c_end = map(int, input().split())
    end_p = (r_end, c_end)
                    
    answer = bfs(start_p, end_p, Map)
    
    print(answer)
