class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        res = ""
        for i in range(len(s)):
            count = 0
            for j in range(i, len(s)):
                if s[j] == '1':
                    count += 1
                if count == k:
                    sub = s[i:j+1]
                    if not res or len(sub) < len(res) or (len(sub) == len(res) and sub < res):
                        res = sub
                    break
        return res