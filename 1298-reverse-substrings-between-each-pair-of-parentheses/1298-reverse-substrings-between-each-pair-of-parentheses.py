class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        current = []
        
        for char in s:
            if char == '(':
                stack.append(current)
                current = []
            elif char == ')':
                current = current[::-1]
                if stack:
                    prev = stack.pop()
                    prev.extend(current)
                    current = prev
            else:
                current.append(char)
                
        return "".join(current)