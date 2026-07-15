def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def subsequencePairCount(self, nums):
        MOD = 10**9 + 7
        dp = {(0, 0): 1}
        
        for x in nums:
            new_dp = {}
            for (g1, g2), count in dp.items():
                new_dp[(g1, g2)] = (new_dp.get((g1, g2), 0) + count) % MOD
                
                ng1 = get_gcd(g1, x)
                new_dp[(ng1, g2)] = (new_dp.get((ng1, g2), 0) + count) % MOD
                
                ng2 = get_gcd(g2, x)
                new_dp[(g1, ng2)] = (new_dp.get((g1, ng2), 0) + count) % MOD
                
            dp = new_dp
            
        ans = 0
        for (g1, g2), count in dp.items():
            if g1 > 0 and g1 == g2:
                ans = (ans + count) % MOD
                
        return ans