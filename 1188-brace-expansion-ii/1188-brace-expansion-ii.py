class Solution(object):
    def braceExpansionII(self, expression):
        def parse(expr):
            stack = [[]]
            group = []
            i = 0
            while i < len(expr):
                if expr[i] == '{':
                    balance = 1
                    j = i + 1
                    while balance > 0:
                        if expr[j] == '{':
                            balance += 1
                        elif expr[j] == '}':
                            balance -= 1
                        j += 1
                    sub = parse(expr[i + 1:j - 1])
                    group.append(sub)
                    i = j
                elif expr[i] == ',':
                    stack[-1].append(group)
                    group = []
                    i += 1
                else:
                    j = i
                    while j < len(expr) and expr[j].isalpha():
                        j += 1
                    group.append([expr[i:j]])
                    i = j
            stack[-1].append(group)
            
            res = set()
            for g in stack[-1]:
                prod = g[0]
                for nxt in g[1:]:
                    prod = {a + b for a in prod for b in nxt}
                res.update(prod)
            return res

        return sorted(list(parse(expression)))