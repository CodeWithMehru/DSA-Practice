class Solution(object):
    def sumAndMultiply(self, n):
        non_zeros = [char for char in str(n) if char != '0']
        
        if not non_zeros:
            return 0
            
        x = int("".join(non_zeros))
        digit_sum = sum(int(char) for char in non_zeros)
        
        return x * digit_sum