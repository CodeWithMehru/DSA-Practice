class Solution(object):
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        
        if m < n:
            return 0
            
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, m + 1):
            for j in range(min(i, n), 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]