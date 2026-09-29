class Solution(object):
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        # A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
            
        # A valid parentheses string must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # We will use an integer as a bitmask to represent the set of reachable balances.
        # The i-th bit will be 1 if a balance of i is possible.
        dp = [0] * n
        dp[0] = 1 << 1  # 2, representing a balance of 1 at (0, 0)

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue
                    
                mask = 0
                if r > 0:
                    mask |= dp[c]
                if c > 0:
                    mask |= dp[c - 1]
                    
                if grid[r][c] == '(':
                    dp[c] = mask << 1
                else:
                    # Right shift naturally drops the 0-th bit (balances that would go negative),
                    # strictly enforcing that at any point open brackets >= close brackets.
                    dp[c] = mask >> 1
                    
        # Check if balance 0 (the 0-th bit) is possible at the destination
        return (dp[n - 1] & 1) == 1