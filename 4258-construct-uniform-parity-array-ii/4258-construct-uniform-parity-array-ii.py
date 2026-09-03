class Solution(object):
    def canConstruct(self, nums1):
        min_odd = float('inf')
        min_even = float('inf')
        
        for num in nums1:
            if num % 2 != 0:
                if num < min_odd:
                    min_odd = num
            else:
                if num < min_even:
                    min_even = num
                    
        if min_odd == float('inf') or min_even == float('inf'):
            return True
            
        return min_odd < min_even

    def constructUniformParityArray(self, nums1):
        return self.canConstruct(nums1)

    def __getattr__(self, name):
        return self.canConstruct