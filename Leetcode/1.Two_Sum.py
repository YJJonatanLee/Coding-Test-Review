class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_nums = sorted(nums)

        i = 0
        j = len(sort_nums) - 1

        while sort_nums[i] + sort_nums[j] != target:
            if sort_nums[i] + sort_nums[j] > target:
                j -= 1
            elif sort_nums[i] + sort_nums[j] < target:
                i += 1

        min = sort_nums[i]
        max = sort_nums[j]

        for i in range(len(nums)):
            if nums[i] == min:
                break

        for j in range(len(nums)-1,-1,-1):
            if nums[j] == max:
                break
        
        return [i,j]
