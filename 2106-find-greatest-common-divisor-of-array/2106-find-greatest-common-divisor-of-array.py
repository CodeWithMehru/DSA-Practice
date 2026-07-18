class Solution:
    def findGCD(self, nums):
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        return get_gcd(min(nums), max(nums))