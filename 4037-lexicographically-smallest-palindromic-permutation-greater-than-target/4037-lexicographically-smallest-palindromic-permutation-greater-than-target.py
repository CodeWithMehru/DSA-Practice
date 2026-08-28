class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
            
        odd_count = sum(1 for v in counts.values() if v % 2 != 0)
        n = len(s)
        
        if (n % 2 == 0 and odd_count > 0) or (n % 2 != 0 and odd_count != 1):
            return ""
            
        middle_char = ""
        if n % 2 != 0:
            for k, v in counts.items():
                if v % 2 != 0:
                    middle_char = k
                    break
                    
        half_counts = {k: v // 2 for k, v in counts.items()}
        half_n = n // 2
        
        L = 0
        temp = half_counts.copy()
        for i in range(half_n):
            if temp.get(target[i], 0) > 0:
                temp[target[i]] -= 1
                L += 1
            else:
                break
                
        if L == half_n:
            cand = target[:half_n] + middle_char + target[:half_n][::-1]
            if cand > target:
                return cand
                
        start_idx = L if L < half_n else half_n - 1
        
        for i in range(start_idx, -1, -1):
            avail = half_counts.copy()
            for j in range(i):
                avail[target[j]] -= 1
                
            best_char = None
            for char_code in range(ord(target[i]) + 1, 123):
                ch = chr(char_code)
                if avail.get(ch, 0) > 0:
                    best_char = ch
                    break
                    
            if best_char:
                avail[best_char] -= 1
                rem = []
                for k, v in avail.items():
                    if v > 0:
                        rem.extend([k] * v)
                rem.sort()
                
                first_half = target[:i] + best_char + "".join(rem)
                return first_half + middle_char + first_half[::-1]
                
        return ""