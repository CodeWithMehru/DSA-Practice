class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        dp = [float('inf')] * n
        ans = float('inf')
        best_so_far = float('inf')
        
        left = 0
        curr_sum = 0
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
                
            if curr_sum == target:
                curr_len = right - left + 1
                if left > 0 and dp[left - 1] != float('inf'):
                    ans = min(ans, curr_len + dp[left - 1])
                best_so_far = min(best_so_far, curr_len)
                
            dp[right] = best_so_far
            
        return ans if ans != float('inf') else -1