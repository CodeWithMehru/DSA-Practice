class Solution(object):
    def reverseDegree(self, s):
        res = 0
        for i, ch in enumerate(s):
            res += (123 - ord(ch)) * (i + 1)
        return res