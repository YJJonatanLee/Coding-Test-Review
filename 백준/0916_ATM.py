n = int(input())
arr = list(map(int, input().split()))

arr_sort = sorted(arr)

num = 0
for i in range(len(arr_sort)):
    wait_num = 0
    for j in range(i + 1):
        wait_num += arr_sort[j]
    num += wait_num

print(num)
