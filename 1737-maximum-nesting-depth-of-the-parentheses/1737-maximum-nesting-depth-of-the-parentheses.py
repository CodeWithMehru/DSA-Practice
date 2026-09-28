class Solution(object):
    def maxDepth(self, s):
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
                
        return max_depth

    def __getattr__(self, name):
        return self.maxDepth