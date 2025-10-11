# class Solution:
#     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
#         combined = [i for i in zip(ages, scores)]
#         combined.sort()

#         dp = [0 for _ in combined]

#         for i in range(len(combined)):
#             age_i, score_i  = combined[i]
#             dp[i] = score_i
#             for j in range(i):
#                 _, score_j, = combined[j]
#                 if score_i > score_j:
#                     dp[i] = max(dp[i], dp[j] + score_i)
        
#         return max(dp)

#         # 5, 5, 4 , 6
from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))  # (age asc, score asc)
        n = len(players)
        dp = [0] * n                          # dp[i] = best team sum ending at i

        for i in range(n):
            age_i, score_i = players[i]
            dp[i] = score_i                   # team with only i
            for j in range(i):
                age_j, score_j = players[j]
                if score_j <= score_i:        # no conflict after age sort
                    dp[i] = max(dp[i], dp[j] + score_i)

        return max(dp)
