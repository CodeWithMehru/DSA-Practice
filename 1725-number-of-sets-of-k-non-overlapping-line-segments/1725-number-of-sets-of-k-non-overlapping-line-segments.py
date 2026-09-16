class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10**9 + 7
        N = n + k - 1
        K = 2 * k
        
        if K > N:
            return 0
            
        num = 1
        den = 1
        for i in range(K):
            num = (num * (N - i)) % MOD
            den = (den * (i + 1)) % MOD
            
        return (num * pow(den, MOD - 2, MOD)) % MOD