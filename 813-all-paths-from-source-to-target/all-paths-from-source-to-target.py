class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)

        cur, res = [], []
        def dfs(node):
            cur.append(node)
            if node == N-1:
                res.append(cur[:])
            else:
                for n in graph[node]:
                    dfs(n)
            cur.pop()
        
        dfs(0)
        return res
        