class Solution(object):
    def lexGreaterPermutation(self, s, target):
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
            
        n = len(s)
        L = 0
        temp_counts = counts.copy()
        
        for char in target:
            if temp_counts.get(char, 0) > 0:
                temp_counts[char] -= 1
                L += 1
            else:
                break
                
        for i in range(min(L, n - 1), -1, -1):
            avail = counts.copy()
            for j in range(i):
                avail[target[j]] -= 1
                
            best_char = None
            for char_code in range(ord(target[i]) + 1, 123):
                char = chr(char_code)
                if avail.get(char, 0) > 0:
                    best_char = char
                    break
            
            if best_char:
                avail[best_char] -= 1
                remainder = []
                for char, count in avail.items():
                    if count > 0:
                        remainder.extend([char] * count)
                
                remainder.sort()
                return target[:i] + best_char + "".join(remainder)
                
        return ""