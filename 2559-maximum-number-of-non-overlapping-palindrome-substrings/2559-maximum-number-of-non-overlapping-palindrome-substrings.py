class Solution(object):
    def maxPalindromes(self, s, k):
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(k, n + 1):
            dp[i] = dp[i - 1]
            
            if i - k >= 0:
                sub = s[i - k:i]
                if sub == sub[::-1]:
                    if dp[i - k] + 1 > dp[i]:
                        dp[i] = dp[i - k] + 1
                        
            if i - k - 1 >= 0:
                sub = s[i - k - 1:i]
                if sub == sub[::-1]:
                    if dp[i - k - 1] + 1 > dp[i]:
                        dp[i] = dp[i - k - 1] + 1
                        
        return dp[n]