class Solution(object):
    def missingMultiple(self, nums, k):
        seen = set(nums)
        res = k
        while res in seen:
            res += k
        return res