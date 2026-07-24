class Solution:
    def uniqueXorTriplets(self, nums):
        u = set(nums)
        px = {a ^ b for a in u for b in u}
        return len({p ^ x for p in px for x in u})