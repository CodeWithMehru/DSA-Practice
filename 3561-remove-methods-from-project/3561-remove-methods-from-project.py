class Solution:
    def remainingMethods(self, n, k, invocations):
        adj = [[] for _ in range(n)]
        for a, b in invocations:
            adj[a].append(b)
            
        suspicious = set([k])
        stack = [k]
        
        while stack:
            node = stack.pop()
            for nxt in adj[node]:
                if nxt not in suspicious:
                    suspicious.add(nxt)
                    stack.append(nxt)
                    
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))
                
        return [i for i in range(n) if i not in suspicious]