class Solution:
    def countCompleteComponents(self, n, edges):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * n
        ans = 0
        
        for i in range(n):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                v_count = 0
                e_count = 0
                
                while stack:
                    curr = stack.pop()
                    v_count += 1
                    e_count += len(adj[curr])
                    
                    for nei in adj[curr]:
                        if not visited[nei]:
                            visited[nei] = True
                            stack.append(nei)
                            
                if e_count == v_count * (v_count - 1):
                    ans += 1
                    
        return ans