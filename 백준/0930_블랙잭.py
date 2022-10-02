N, M = map(int, input().split())
num_list = list(map(int, input().split()))

max_sum = 0
for x in num_list:
    for y in num_list:
        for z in num_list:
            if (x==y)|(y==z)|(x==z):
                continue
            ch_ = x+y+z
            if (max_sum < ch_) & (M >= ch_):
                max_sum = ch_
print(max_sum)
