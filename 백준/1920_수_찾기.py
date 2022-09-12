def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

N = int(input())
A_array = list(map(int, input().split()))
A_array_sort = sorted(A_array)

M = int(input())
target_array = list(map(int, input().split()))

for i in target_array:
    result = binary_search(A_array_sort, 0, N - 1, i)
    print(result)
