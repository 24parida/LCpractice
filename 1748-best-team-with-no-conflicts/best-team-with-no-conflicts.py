class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        combined = [i for i in zip(ages, scores)]
        combined.sort()

        dp = [0 for _ in combined]

        for i in range(len(combined)):
            age_i, score_i  = combined[i]
            dp[i] = score_i
            for j in range(i):
                _, score_j, = combined[j]
                if score_j <= score_i:
                    dp[i] = max(dp[i], dp[j] + score_i)
        
        return max(dp)