class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        
        # The maximum product can either be:
        # 1. The three largest positive numbers
        # 2. The two smallest negative numbers (which make a positive product) * the largest positive number
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])