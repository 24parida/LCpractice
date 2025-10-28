class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        cache = {}
        def dfs(i, j):
            if (i,j) in cache:
                return cache[(i,j)]

            if j >= len(triangle):
                return 0
            
            cur = triangle[j][i]
            left = dfs(i, j+1)
            right = dfs(i+1, j+1)
            cache[(i, j)] = cur + min(right, left)
            return cache[(i, j)]
        
        return dfs(0, 0)