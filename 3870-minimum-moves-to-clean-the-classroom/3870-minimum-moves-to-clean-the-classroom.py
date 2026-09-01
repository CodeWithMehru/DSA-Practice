class Solution(object):
    def minMoves(self, classroom, energy):
        from collections import deque
        
        m = len(classroom)
        n = len(classroom[0])
        
        litter_map = {}
        litter_count = 0
        start_r = start_c = 0
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r = r
                    start_c = c
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1
                    
        if litter_count == 0:
            return 0
            
        target_mask = (1 << litter_count) - 1
        max_energy = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)]
        
        queue = deque([(start_r, start_c, 0, energy, 0)])
        max_energy[start_r][start_c][0] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, e, steps = queue.popleft()
            
            if e == 0:
                continue
                
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    ne = e - 1
                    nmask = mask
                    cell = classroom[nr][nc]
                    
                    if cell == 'L':
                        nmask |= (1 << litter_map[(nr, nc)])
                        if nmask == target_mask:
                            return steps + 1
                    elif cell == 'R':
                        ne = energy
                        
                    if ne > max_energy[nr][nc][nmask]:
                        max_energy[nr][nc][nmask] = ne
                        queue.append((nr, nc, nmask, ne, steps + 1))
                        
        return -1