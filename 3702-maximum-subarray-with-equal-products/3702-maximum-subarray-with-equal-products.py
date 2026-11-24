class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        n = len(nums)
        ans = 2  # Any subarray of length 2 satisfies prod(a, b) == gcd(a, b) * lcm(a, b)

        for i in range(n):
            curr_prod = nums[i]
            curr_gcd = nums[i]
            curr_lcm = nums[i]

            for j in range(i + 1, n):
                val = nums[j]
                curr_prod *= val
                curr_gcd = gcd(curr_gcd, val)
                curr_lcm = (curr_lcm * val) // gcd(curr_lcm, val)

                # Since 1 <= nums[i] <= 10, lcm <= lcm(1..10) = 2520 and gcd <= 10
                if curr_prod > 25200:
                    break

                if curr_prod == curr_lcm * curr_gcd:
                    if j - i + 1 > ans:
                        ans = j - i + 1

        return ans