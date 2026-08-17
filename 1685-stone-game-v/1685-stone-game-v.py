class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_L = [[0] * n for _ in range(n)]
        max_R = [[0] * n for _ in range(n)]
        
        for i in range(n):
            max_L[i][i] = stoneValue[i]
            max_R[i][i] = stoneValue[i]
            
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                target = prefix[j+1] + prefix[i]
                
                low, high = i, j - 1
                m = i - 1
                while low <= high:
                    mid = (low + high) // 2
                    if prefix[mid+1] * 2 <= target:
                        m = mid
                        low = mid + 1
                    else:
                        high = mid - 1
                        
                res = 0
                
                if m >= i:
                    res = max_L[i][m]
                    
                if m >= i and prefix[m+1] * 2 == target:
                    if max_R[m+1][j] > res:
                        res = max_R[m+1][j]
                elif m + 1 <= j - 1:
                    if max_R[m+2][j] > res:
                        res = max_R[m+2][j]
                        
                dp[i][j] = res
                
                current_sum_plus_dp = prefix[j+1] - prefix[i] + res
                
                if max_L[i][j-1] > current_sum_plus_dp:
                    max_L[i][j] = max_L[i][j-1]
                else:
                    max_L[i][j] = current_sum_plus_dp
                    
                if max_R[i+1][j] > current_sum_plus_dp:
                    max_R[i][j] = max_R[i+1][j]
                else:
                    max_R[i][j] = current_sum_plus_dp
                    
        return dp[0][n-1]