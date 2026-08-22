class Solution(object):
    def checkDivisibility(self, n):
        temp = n
        digit_sum = 0
        digit_prod = 1
        
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_prod *= digit
            temp //= 10
            
        return n % (digit_sum + digit_prod) == 0