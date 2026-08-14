class Solution:
    def maximumLengthSubstring(self, s):
        freq = {}
        max_len = 0
        left = 0
        
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1
                
            if right - left + 1 > max_len:
                max_len = right - left + 1
                
        return max_len