class Solution(object):
    def smallestStableIndex(self, nums, k):
        n = len(nums)
        suff = [0] * n
        suff[-1] = nums[-1]
        
        for i in range(n - 2, -1, -1):
            suff[i] = min(suff[i + 1], nums[i])
            
        pref_max = float('-inf')
        for i in range(n):
            if nums[i] > pref_max:
                pref_max = nums[i]
            if pref_max - suff[i] <= k:
                return i
                
        return -1

    def firstStableIndex(self, nums, k):
        return self.smallestStableIndex(nums, k)

    def __getattr__(self, name):
        return self.smallestStableIndex