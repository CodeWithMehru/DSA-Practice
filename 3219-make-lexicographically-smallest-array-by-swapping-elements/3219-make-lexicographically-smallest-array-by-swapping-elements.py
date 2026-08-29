class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        pairs = sorted([(nums[i], i) for i in range(n)])
        
        res = [0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and pairs[j+1][0] - pairs[j][0] <= limit:
                j += 1
            
            indices = sorted([pairs[k][1] for k in range(i, j + 1)])
            
            for k in range(i, j + 1):
                res[indices[k - i]] = pairs[k][0]
                
            i = j + 1
            
        return res