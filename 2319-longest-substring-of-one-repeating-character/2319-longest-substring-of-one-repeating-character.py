class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        N = 1
        while N < n:
            N *= 2
            
        pref_len = [0] * (2 * N)
        suff_len = [0] * (2 * N)
        max_len = [0] * (2 * N)
        pref_char = [0] * (2 * N)
        suff_char = [0] * (2 * N)
        sz = [0] * (2 * N)
        
        s_bytes = [ord(c) for c in s]
        
        for i in range(n):
            idx = N + i
            pref_len[idx] = 1
            suff_len[idx] = 1
            max_len[idx] = 1
            pref_char[idx] = s_bytes[i]
            suff_char[idx] = s_bytes[i]
            sz[idx] = 1
            
        for i in range(n, N):
            idx = N + i
            sz[idx] = 1
            pref_char[idx] = -1 - i
            suff_char[idx] = -1 - i
            
        for i in range(N - 1, 0, -1):
            left = 2 * i
            right = 2 * i + 1
            sz[i] = sz[left] + sz[right]
            
            pref_char[i] = pref_char[left]
            suff_char[i] = suff_char[right]
            
            pl = pref_len[left]
            if pl == sz[left] and pref_char[left] == pref_char[right]:
                pl += pref_len[right]
            pref_len[i] = pl
                
            sl = suff_len[right]
            if sl == sz[right] and suff_char[right] == suff_char[left]:
                sl += suff_len[left]
            suff_len[i] = sl
                
            max_l = max_len[left]
            max_r = max_len[right]
            m_len = max_l if max_l > max_r else max_r
            if suff_char[left] == pref_char[right]:
                cross = suff_len[left] + pref_len[right]
                if cross > m_len:
                    m_len = cross
            max_len[i] = m_len
            
        ans = []
        q_bytes = [ord(c) for c in queryCharacters]
        
        for i in range(len(queryIndices)):
            idx = N + queryIndices[i]
            c = q_bytes[i]
            
            pref_char[idx] = c
            suff_char[idx] = c
            
            idx //= 2
            while idx > 0:
                left = 2 * idx
                right = 2 * idx + 1
                
                pref_char[idx] = pref_char[left]
                suff_char[idx] = suff_char[right]
                
                pl = pref_len[left]
                if pl == sz[left] and pref_char[left] == pref_char[right]:
                    pl += pref_len[right]
                pref_len[idx] = pl
                    
                sl = suff_len[right]
                if sl == sz[right] and suff_char[right] == suff_char[left]:
                    sl += suff_len[left]
                suff_len[idx] = sl
                    
                max_l = max_len[left]
                max_r = max_len[right]
                m_len = max_l if max_l > max_r else max_r
                if suff_char[left] == pref_char[right]:
                    cross = suff_len[left] + pref_len[right]
                    if cross > m_len:
                        m_len = cross
                max_len[idx] = m_len
                
                idx //= 2
                
            ans.append(max_len[1])
            
        return ans