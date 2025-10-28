class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        N, M = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (M+1) for _ in range(N+1)]
        dp[N][M-1] = 1
        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                if obstacleGrid[i][j]:
                    continue
                
                down = dp[i+1][j]
                right = dp[i][j+1]
                dp[i][j] = down + right
        
        return dp[0][0]