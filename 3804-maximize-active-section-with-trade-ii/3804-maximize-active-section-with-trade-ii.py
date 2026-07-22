import bisect

class SparseTable:
    def __init__(self, data):
        self.n = len(data)
        if self.n == 0:
            self.st = []
            return
        self.k = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.k)]
        self.st[0] = list(data)
        for j in range(1, self.k):
            step = 1 << (j - 1)
            for i in range(self.n - (1 << j) + 1):
                self.st[j][i] = max(self.st[j-1][i], self.st[j-1][i + step])

    def query(self, L, R):
        if L > R: return 0
        j = (R - L + 1).bit_length() - 1
        return max(self.st[j][L], self.st[j][R - (1 << j) + 1])

class Solution:
    def maxActiveSectionsAfterTrade(self, s, queries):
        n = len(s)
        total_ones = s.count('1')
        
        runs = []
        i = 0
        while i < n:
            char = s[i]
            start = i
            while i < n and s[i] == char:
                i += 1
            runs.append((char, start, i - 1, i - start))
            
        m_runs = len(runs)
        run_starts = [r[1] for r in runs]
        
        val = [0] * m_runs
        for idx in range(1, m_runs - 1):
            if runs[idx][0] == '1':
                val[idx] = runs[idx-1][3] + runs[idx+1][3]
                
        st = SparseTable(val)
        ans = []
        
        for l, r in queries:
            k = bisect.bisect_right(run_starts, l) - 1
            m = bisect.bisect_right(run_starts, r) - 1
            
            if k >= m - 1:
                ans.append(total_ones)
                continue
                
            max_gain = 0
            
            if runs[k+1][0] == '1':
                A = runs[k][2] - l + 1
                if k + 2 == m:
                    B = r - runs[m][1] + 1
                else:
                    B = runs[k+2][3]
                if A + B > max_gain:
                    max_gain = A + B
                    
            if m - 1 > k + 1 and runs[m-1][0] == '1':
                B = r - runs[m][1] + 1
                A = runs[m-2][3]
                if A + B > max_gain:
                    max_gain = A + B
                    
            if m - 2 >= k + 2:
                mx = st.query(k + 2, m - 2)
                if mx > max_gain:
                    max_gain = mx
                    
            ans.append(total_ones + max_gain)
            
        return ans