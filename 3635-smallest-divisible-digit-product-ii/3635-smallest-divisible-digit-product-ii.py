class Solution:
    def smallestNumber(self, num, t):
        req2 = req3 = req5 = req7 = 0
        temp = t
        while temp % 2 == 0: 
            req2 += 1
            temp //= 2
        while temp % 3 == 0: 
            req3 += 1
            temp //= 3
        while temp % 5 == 0: 
            req5 += 1
            temp //= 5
        while temp % 7 == 0: 
            req7 += 1
            temp //= 7
            
        if temp > 1: 
            return "-1"
            
        dp = [[float('inf')] * 40 for _ in range(60)]
        dp[0][0] = 0
        
        for i in range(60):
            for j in range(40):
                if i == 0 and j == 0: 
                    continue
                res = float('inf')
                for p2, p3 in [(1,0), (0,1), (2,0), (1,1), (3,0), (0,2)]:
                    ni = max(0, i - p2)
                    nj = max(0, j - p3)
                    if 1 + dp[ni][nj] < res:
                        res = 1 + dp[ni][nj]
                dp[i][j] = res
                
        FACTORS = {
            1: (0,0,0,0),
            2: (1,0,0,0),
            3: (0,1,0,0),
            4: (2,0,0,0),
            5: (0,0,1,0),
            6: (1,1,0,0),
            7: (0,0,0,1),
            8: (3,0,0,0),
            9: (0,2,0,0)
        }
        
        N = len(num)
        p2 = [0] * (N + 1)
        p3 = [0] * (N + 1)
        p5 = [0] * (N + 1)
        p7 = [0] * (N + 1)
        
        for i in range(N):
            d = int(num[i])
            if d > 0:
                f = FACTORS[d]
                p2[i+1] = p2[i] + f[0]
                p3[i+1] = p3[i] + f[1]
                p5[i+1] = p5[i] + f[2]
                p7[i+1] = p7[i] + f[3]
            else:
                p2[i+1] = p2[i]
                p3[i+1] = p3[i]
                p5[i+1] = p5[i]
                p7[i+1] = p7[i]
                
        zero_idx = num.find('0')
        
        if zero_idx == -1 and p2[N] >= req2 and p3[N] >= req3 and p5[N] >= req5 and p7[N] >= req7:
            return num
            
        for i in range(N - 1, -1, -1):
            if zero_idx != -1 and i > zero_idx:
                continue
                
            curr_d = int(num[i])
            for d in range(curr_d + 1, 10):
                f = FACTORS[d]
                rem2 = max(0, req2 - p2[i] - f[0])
                rem3 = max(0, req3 - p3[i] - f[1])
                rem5 = max(0, req5 - p5[i] - f[2])
                rem7 = max(0, req7 - p7[i] - f[3])
                
                if dp[rem2][rem3] + rem5 + rem7 <= N - 1 - i:
                    ans = list(num[:i])
                    ans.append(str(d))
                    
                    curr_rem2, curr_rem3, curr_rem5, curr_rem7 = rem2, rem3, rem5, rem7
                    for pos in range(i + 1, N):
                        for next_d in range(1, 10):
                            nf = FACTORS[next_d]
                            nxt_rem2 = max(0, curr_rem2 - nf[0])
                            nxt_rem3 = max(0, curr_rem3 - nf[1])
                            nxt_rem5 = max(0, curr_rem5 - nf[2])
                            nxt_rem7 = max(0, curr_rem7 - nf[3])
                            
                            if dp[nxt_rem2][nxt_rem3] + nxt_rem5 + nxt_rem7 <= N - 1 - pos:
                                ans.append(str(next_d))
                                curr_rem2, curr_rem3, curr_rem5, curr_rem7 = nxt_rem2, nxt_rem3, nxt_rem5, nxt_rem7
                                break
                    return "".join(ans)
                    
        L = max(N + 1, dp[req2][req3] + req5 + req7)
        ans = []
        curr_rem2, curr_rem3, curr_rem5, curr_rem7 = req2, req3, req5, req7
        for pos in range(L):
            for next_d in range(1, 10):
                nf = FACTORS[next_d]
                nxt_rem2 = max(0, curr_rem2 - nf[0])
                nxt_rem3 = max(0, curr_rem3 - nf[1])
                nxt_rem5 = max(0, curr_rem5 - nf[2])
                nxt_rem7 = max(0, curr_rem7 - nf[3])
                
                if dp[nxt_rem2][nxt_rem3] + nxt_rem5 + nxt_rem7 <= L - 1 - pos:
                    ans.append(str(next_d))
                    curr_rem2, curr_rem3, curr_rem5, curr_rem7 = nxt_rem2, nxt_rem3, nxt_rem5, nxt_rem7
                    break
        return "".join(ans)