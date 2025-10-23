class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x, y, r1 = bombs[i]
                x2, y2, r2 = bombs[j]

                dist = lambda x, y, i, j: sqrt((x-i)**2 + (y-j)**2)
                distance = dist(x,y,x2,y2)

                if distance <= r1:
                    graph[(i, x, y)].append((j, x2, y2))
                if distance <= r2:
                    graph[(j, x2, y2)].append((i, x, y))
        

        
        def dfs(node):
            if node in self.visited:
                return 0
            self.visited.add(node)
            largest_neighbor = 0
            for neigh in graph[node]: largest_neighbor += dfs(neigh)
            return 1 + largest_neighbor

        res = 1
        for bomb in list(graph.keys()):
            self.visited = set()
            res = max(dfs(bomb), res)
        
        return res