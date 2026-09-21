class Solution(object):
    def findXValue(self, nums, k):
        res = [0] * k
        counts = [0] * k
        
        for num in nums:
            val = num % k
            new_counts = [0] * k
            new_counts[val] += 1
            
            for r in range(k):
                if counts[r] > 0:
                    new_counts[(r * val) % k] += counts[r]
                    
            for r in range(k):
                res[r] += new_counts[r]
                counts[r] = new_counts[r]
                
        return res

    def __getattr__(self, name):
        return self.findXValue