class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        return (xCenter - closest_x) ** 2 + (yCenter - closest_y) ** 2 <= radius ** 2