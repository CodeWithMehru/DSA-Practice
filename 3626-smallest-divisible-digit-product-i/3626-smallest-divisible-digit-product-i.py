class Solution:
    def smallestNumber(self, n, t):
        while True:
            temp = n
            prod = 1
            while temp > 0:
                prod *= temp % 10
                temp //= 10
            if prod % t == 0:
                return n
            n += 1