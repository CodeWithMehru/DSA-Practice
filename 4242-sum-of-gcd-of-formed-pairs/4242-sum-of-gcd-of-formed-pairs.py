class Solution:
    def gcdSum(self, nums):
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
            
        n = len(nums)
        prefix_gcd = [0] * n
        curr_max = nums[0]
        
        
        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]
            prefix_gcd[i] = get_gcd(nums[i], curr_max)
            
        
        prefix_gcd.sort()
        
        ans = 0
        left = 0
        right = n - 1
        
        
        while left < right:
            ans += get_gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
            
        return ans