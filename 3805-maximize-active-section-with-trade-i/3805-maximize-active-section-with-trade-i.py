class Solution:
    def maxActiveSectionsAfterTrade(self, s):
        base_ones = s.count('1')
        t = "1" + s + "1"
        
        groups = []
        n = len(t)
        i = 0
        while i < n:
            char = t[i]
            count = 0
            while i < n and t[i] == char:
                count += 1
                i += 1
            groups.append((char, count))
            
        max_c = 0
        for char, count in groups:
            if char == '0':
                if count > max_c:
                    max_c = count
                    
        max_delta = 0
        for idx in range(1, len(groups) - 1):
            char, count = groups[idx]
            if char == '1':
                prev_char, prev_count = groups[idx - 1]
                next_char, next_count = groups[idx + 1]
                
                if prev_char == '0' and next_char == '0':
                    L = count
                    A = prev_count
                    B = next_count
                    delta = max(A + B, max_c - L)
                    if delta > max_delta:
                        max_delta = delta
                        
        return base_ones + max_delta