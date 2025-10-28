class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]


        dp = triangle[-1]
        for j in range(len(triangle)-2, -1, -1):
            new_dp = []
            for i in range(len(triangle[j])):
                new_dp.append(triangle[j][i] + min(dp[i], dp[i+1]))
            dp = new_dp
        
        return dp[0]