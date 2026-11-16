class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            new_s = []
            for i in range(0, len(s), k):
                group_sum = sum(int(char) for char in s[i:i+k])
                new_s.append(str(group_sum))
            s = "".join(new_s)
        return s