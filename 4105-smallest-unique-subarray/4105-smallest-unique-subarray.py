import random

class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)
        if n == 1:
            return 1

        # Quick O(n) check for length 1
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        if 1 in freq.values():
            return 1

        MOD1, MOD2 = 1000000007, 1000000009
        BASE1 = random.randint(100003, 200000)
        BASE2 = random.randint(200003, 300000)

        p1 = [0] * (n + 1)
        p2 = [0] * (n + 1)
        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)

        for i, x in enumerate(nums):
            p1[i + 1] = (p1[i] * BASE1 + x) % MOD1
            p2[i + 1] = (p2[i] * BASE2 + x) % MOD2
            pow1[i + 1] = (pow1[i] * BASE1) % MOD1
            pow2[i + 1] = (pow2[i] * BASE2) % MOD2

        def has_unique(length):
            seen = set()
            dup = set()
            b1 = pow1[length]
            b2 = pow2[length]
            for i in range(n - length + 1):
                h1 = (p1[i + length] - p1[i] * b1) % MOD1
                h2 = (p2[i + length] - p2[i] * b2) % MOD2
                h = (h1 << 32) | h2
                if h in seen:
                    dup.add(h)
                else:
                    seen.add(h)
            return len(seen) > len(dup)

        lo, hi = 2, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo