class Solution(object):
    def maxItems(self, items, budget):
        max_factor = max(f for f, _ in items)
        freq = [0] * (max_factor + 1)
        min_price = float('inf')

        for f, p in items:
            freq[f] += 1
            if p < min_price:
                min_price = p

        
        div_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f]:
                total = 0
                for mult in range(f, max_factor + 1, f):
                    total += freq[mult]
                div_count[f] = total

        
        dp = [-1] * (budget + 1)
        dp[0] = 0

        for f, p in items:
            if p <= budget:
                gain = div_count[f]
                for c in range(budget, p - 1, -1):
                    if dp[c - p] != -1 and dp[c - p] + gain > dp[c]:
                        dp[c] = dp[c - p] + gain

        
        ans = 0
        for c in range(budget + 1):
            if dp[c] != -1:
                total_copies = dp[c] + (budget - c) // min_price
                if total_copies > ans:
                    ans = total_copies

        return ans

    def __getattr__(self, name):
        return self.maxItems