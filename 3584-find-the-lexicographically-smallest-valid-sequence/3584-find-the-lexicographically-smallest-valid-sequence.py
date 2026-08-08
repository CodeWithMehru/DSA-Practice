class Solution:
    def validSequence(self, word1, word2):
        N = len(word1)
        M = len(word2)
        
        last_match = [-1] * M
        p1 = N - 1
        for p2 in range(M - 1, -1, -1):
            while p1 >= 0 and word1[p1] != word2[p2]:
                p1 -= 1
            if p1 >= 0:
                last_match[p2] = p1
                p1 -= 1
            else:
                break
                
        ans = []
        changed = False
        j = 0
        
        for i in range(N):
            if j == M:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            elif not changed and (j + 1 == M or last_match[j+1] > i):
                changed = True
                ans.append(i)
                j += 1
                
        if len(ans) == M:
            return ans
        return []