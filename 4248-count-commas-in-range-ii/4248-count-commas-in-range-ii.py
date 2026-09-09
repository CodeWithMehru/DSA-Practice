class Solution(object):
    def countCommas(self, n):
        ans = 0
        base = 1000
        while n >= base:
            ans += n - base + 1
            base *= 1000
        return ans

    def __getattr__(self, name):
        return self.countCommas