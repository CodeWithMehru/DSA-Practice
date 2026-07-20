class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        flat = [val for row in grid for val in row]
        k = k % len(flat)
        flat = flat[-k:] + flat[:-k]
        ans = []
        for i in range(m):
            ans.append(flat[i * n : (i + 1) * n])
        return ans