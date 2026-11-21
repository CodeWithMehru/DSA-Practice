from collections import deque

class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = list(parent)
        last_seen = [-1] * 26
        saved = [-1] * n
        stack = [0]

        while stack:
            u = stack.pop()
            if u >= 0:
                c = ord(s[u]) - 97
                if u != 0 and last_seen[c] != -1:
                    new_parent[u] = last_seen[c]
                saved[u] = last_seen[c]
                stack.append(~u)
                last_seen[c] = u
                for v in children[u]:
                    stack.append(v)
            else:
                node = ~u
                last_seen[ord(s[node]) - 97] = saved[node]

        size = [1] * n
        deg = [0] * n
        for i in range(1, n):
            deg[new_parent[i]] += 1

        queue = deque(i for i in range(n) if deg[i] == 0)
        while queue:
            u = queue.popleft()
            p = new_parent[u]
            if p != -1:
                size[p] += size[u]
                deg[p] -= 1
                if deg[p] == 0:
                    queue.append(p)

        return size