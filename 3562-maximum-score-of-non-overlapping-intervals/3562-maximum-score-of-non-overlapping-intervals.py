class Solution(object):
    def maximumWeight(self, intervals):
        import bisect
        
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        arr.sort(key=lambda x: x[1])
        
        R = [x[1] for x in arr]
        N = len(arr)
        
        dp = [[(-1, []) for _ in range(N + 1)] for _ in range(5)]
        for i in range(N + 1):
            dp[0][i] = (0, [])
            
        for i in range(1, N + 1):
            l, r, w, orig_idx = arr[i-1]
            j = bisect.bisect_left(R, l)
            
            for k in range(1, 5):
                opt1 = dp[k][i-1]
                
                prev = dp[k-1][j]
                if prev[0] != -1:
                    opt2 = (prev[0] + w, sorted(prev[1] + [orig_idx]))
                else:
                    opt2 = (-1, [])
                    
                if opt1[0] != opt2[0]:
                    dp[k][i] = opt1 if opt1[0] > opt2[0] else opt2
                else:
                    if opt1[0] == -1:
                        dp[k][i] = opt1
                    else:
                        dp[k][i] = opt1 if opt1[1] < opt2[1] else opt2

        best = (-1, [])
        for k in range(1, 5):
            opt1 = best
            opt2 = dp[k][N]
            if opt1[0] != opt2[0]:
                best = opt1 if opt1[0] > opt2[0] else opt2
            else:
                if opt1[0] != -1:
                    best = opt1 if opt1[1] < opt2[1] else opt2
                    
        return best[1]