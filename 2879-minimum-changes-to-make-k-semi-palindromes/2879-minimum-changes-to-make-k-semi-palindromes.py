class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                divisors[j].append(i)
                
        def get_changes(sub):
            m = len(sub)
            res = float('inf')
            for d in divisors[m]:
                changes = 0
                for i in range(d):
                    l, r = i, m - d + i
                    while l < r:
                        if sub[l] != sub[r]:
                            changes += 1
                        l += d
                        r -= d
                if changes < res:
                    res = changes
            return res

        cost = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_changes(s[i:j + 1])

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(2, n + 1):
            for j in range(1, k + 1):
                for prev in range(2 * (j - 1), i - 1):
                    if dp[prev][j - 1] != float('inf'):
                        val = dp[prev][j - 1] + cost[prev][i - 1]
                        if val < dp[i][j]:
                            dp[i][j] = val
                        
        return dp[n][k]