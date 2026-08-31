class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        if not head or not head.next or not head.next.next:
            return [-1, -1]
            
        critical_points = []
        prev = head
        curr = head.next
        idx = 1
        
        while curr.next:
            nxt = curr.next
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                critical_points.append(idx)
                
            prev = curr
            curr = curr.next
            idx += 1
            
        if len(critical_points) < 2:
            return [-1, -1]
            
        min_dist = float('inf')
        for i in range(1, len(critical_points)):
            min_dist = min(min_dist, critical_points[i] - critical_points[i-1])
            
        max_dist = critical_points[-1] - critical_points[0]
        
        return [min_dist, max_dist]