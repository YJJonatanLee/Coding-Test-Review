n = 11
arr = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

arr_sort = sorted(arr, key = lambda x: (x[1], x[0]))

arr_sort
