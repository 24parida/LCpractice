class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visit = set()
        islands = 0
        R, C = len(grid), len(grid[0])

        def bfs(r, c):
            if min(r,c) < 0 or r == R or c == C or grid[r][c] == "0" or (r,c) in visit: return
            visit.add((r,c))
            bfs(r + 1,c)
            bfs(r - 1,c)
            bfs(r,c + 1)
            bfs(r,c -1)


        for r in range(R):
            for c in range(C):
                if (r,c) in visit or grid[r][c] == "0": continue
                bfs(r,c)
                islands += 1

        return islands


        