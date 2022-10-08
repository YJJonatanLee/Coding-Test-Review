nums_len = int(input())

nums = list(map(int, input().split()))

memo = [1] * nums_len

for i, num in reversed(list(enumerate(nums))):
    for j in range(i, nums_len):
        if num < nums[j]:
            memo[i] = max(memo[i], memo[j] + 1)
            
print(max(memo))
