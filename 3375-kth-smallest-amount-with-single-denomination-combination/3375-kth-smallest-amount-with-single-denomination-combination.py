class Solution(object):
    def findKthSmallest(self, coins, k):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)
            
        n = len(coins)
        subsets = []
        
        for i in range(1, 1 << n):
            lcm_val = 1
            set_bits = 0
            for j in range(n):
                if i & (1 << j):
                    lcm_val = lcm(lcm_val, coins[j])
                    set_bits += 1
            
            sign = 1 if set_bits % 2 == 1 else -1
            subsets.append((lcm_val, sign))
            
        low = 1
        high = min(coins) * k
        
        while low <= high:
            mid = (low + high) // 2
            
            count = 0
            for lcm_val, sign in subsets:
                count += sign * (mid // lcm_val)
                
            if count >= k:
                high = mid - 1
            else:
                low = mid + 1
                
        return low