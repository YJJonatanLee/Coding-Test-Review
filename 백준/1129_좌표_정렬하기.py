
N = int(input())

points = []
for _ in range(N):
    points.append(tuple(map(int, input().split())))

for x, y in sorted(points, key=lambda x : (x[0], x[1])):
    print(x, y)
