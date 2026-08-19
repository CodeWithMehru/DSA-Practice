import collections

class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        masks = collections.defaultdict(int)
        
        for r, c in reservedSeats:
            masks[r] |= (1 << c)
            
        ans = 2 * n
        
        for mask in masks.values():
            ans -= 2
            if (mask & 60) == 0 and (mask & 960) == 0:
                ans += 2
            elif (mask & 60) == 0:
                ans += 1
            elif (mask & 960) == 0:
                ans += 1
            elif (mask & 240) == 0:
                ans += 1
                
        return ans