class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.graph = collections.defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            self.graph[a].append((b, value))
            self.graph[b].append((a, 1/value))

        res = []
        for a, b in queries:
            self.visited = set()
            res.append(self.dfs(a, b))

        return res

    def dfs(self, a, b):
        if a in self.graph and a == b:
            return 1.0
        if (a not in self.graph or b not in self.graph) or a in self.visited:
            return -1.0

        self.visited.add(a)
        
        for n, weight in self.graph[a]:
            res = self.dfs(n, b)
            if res != -1.0:
                return weight * res
        
        return -1.0
