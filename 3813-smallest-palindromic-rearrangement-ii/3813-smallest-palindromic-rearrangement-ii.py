import math

class Solution:
    def kthPalindrome(self, s, k):
        cnt = [0] * 26
        for char in s:
            cnt[ord(char) - 97] += 1
            
        half_cnt = [0] * 26
        mid_char = ""
        for i in range(26):
            if cnt[i] % 2 != 0:
                mid_char = chr(i + 97)
            half_cnt[i] = cnt[i] // 2
            
        N = sum(half_cnt)
        P = math.factorial(N)
        for count in half_cnt:
            P //= math.factorial(count)
            
        if k > P:
            return ""
            
        left_half = []
        for _ in range(N):
            for i in range(26):
                if half_cnt[i] > 0:
                    P_next = P * half_cnt[i] // N
                    if k > P_next:
                        k -= P_next
                    else:
                        left_half.append(chr(i + 97))
                        half_cnt[i] -= 1
                        P = P_next
                        N -= 1
                        break
                        
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]

    def smallestPalindromicRearrangement(self, s, k):
        return self.kthPalindrome(s, k)
        
    def smallestPalindrome(self, s, k):
        return self.kthPalindrome(s, k)