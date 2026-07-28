class Solution:
    def smallestPalindrome(self, s):
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1
            
        half = []
        mid = ""
        
        for i in range(26):
            if cnt[i] % 2 != 0:
                mid = chr(i + 97)
            if cnt[i] > 0:
                half.append(chr(i + 97) * (cnt[i] // 2))
                
        left = "".join(half)
        return left + mid + left[::-1]