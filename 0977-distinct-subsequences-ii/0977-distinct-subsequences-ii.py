class Solution(object):
    def distinctSubseqII(self, s):
        mod = 10**9 + 7
        ends = [0] * 26
        total = 0
        
        for char in s:
            idx = ord(char) - 97
            new_add = (total + 1 - ends[idx]) % mod
            ends[idx] = (ends[idx] + new_add) % mod
            total = (total + new_add) % mod
            
        return total