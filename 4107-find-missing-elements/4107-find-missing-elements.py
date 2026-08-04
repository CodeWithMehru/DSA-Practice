class Solution:
    def findMissingElements(self, nums):
        num_set = set(nums)
        return [i for i in range(min(nums), max(nums) + 1) if i not in num_set]