class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        n = len(arr)
        counts = [0] * (n + 1)
        
        for num in arr:
            counts[min(num, n)] += 1
            
        ans = 0
        for val in range(1, n + 1):
            ans = min(ans + counts[val], val)
            
        return ans