class Solution:
    def gcdValues(self, nums, queries):
        max_val = max(nums)
        cnt = [0] * (max_val + 1)
        for num in nums:
            cnt[num] += 1
            
        gcd_count = [0] * (max_val + 1)
        
        for i in range(max_val, 0, -1):
            c = sum(cnt[i::i])
            gcd_count[i] = c * (c - 1) // 2
            for j in range(2 * i, max_val + 1, i):
                gcd_count[i] -= gcd_count[j]
                
        prefix = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix[i] = prefix[i-1] + gcd_count[i]
            
        import bisect
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix, q)
            ans.append(idx)
            
        return ans