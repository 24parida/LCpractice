class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0

        directions = [(-1, 0), (1, 0), (0, 1), (0,-1)]
        visited = set()

        N = len(grid)
        M = len(grid[0])
        is_in_bounds = lambda x,y: (x >= 0 and x < N) and (y >= 0 and y < M)

        def bfs(nodeX, nodeY):
            q = collections.deque([(nodeX, nodeY)])
            visited.add((nodeX, nodeY))
            touches_border = False
            while q:
                x,y = q.popleft()
                if x == N-1 or y == M-1 or x == 0 or y == 0:
                    touches_border = True
                
                for nx, ny in directions:
                    new_x, new_y = x+nx, y+ny
                    if is_in_bounds(new_x, new_y) and (new_x, new_y) not in visited and grid[new_x][new_y] == 0:
                        visited.add((new_x, new_y))
                        q.append((new_x, new_y))
            
            return not touches_border
        
        for i in range(N):
            for j in range(M):
                if (i,j) not in visited and grid[i][j] == 0:
                    res += 1 if bfs(i,j) else 0
        
        return res

                
