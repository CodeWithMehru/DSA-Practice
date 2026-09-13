import collections

class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        pts1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        pts2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]
        
        counts = collections.defaultdict(int)
        for r1, c1 in pts1:
            for r2, c2 in pts2:
                counts[(r2 - r1, c2 - c1)] += 1
                
        return max(counts.values()) if counts else 0