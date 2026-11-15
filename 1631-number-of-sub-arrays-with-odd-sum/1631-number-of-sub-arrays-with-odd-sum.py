class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1
        current_sum = 0
        res = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 == 1:
                res = (res + even_count) % MOD
                odd_count += 1
            else:
                res = (res + odd_count) % MOD
                even_count += 1
                
        return res