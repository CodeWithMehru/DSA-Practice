class Solution:
    def minimumPushes(self, word):
        freq = [0] * 26
        for c in word:
            freq[ord(c) - 97] += 1
            
        freq.sort(reverse=True)
        
        ans = 0
        for i in range(26):
            if freq[i] == 0:
                break
            ans += freq[i] * ((i // 8) + 1)
            
        return ans