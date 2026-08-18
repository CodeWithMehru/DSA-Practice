class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        count = {}
        
        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            seen = set()
            for num in subarray:
                if num not in seen:
                    count[num] = count.get(num, 0) + 1
                    seen.add(num)
                    
        largest = -1
        for num, freq in count.items():
            if freq == 1:
                largest = max(largest, num)
                
        return largest