class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        lpx, lpy = points[0]
        for i in range(1, len(points)):
            dx = abs(points[i][0] - lpx)
            dy = abs(points[i][1] - lpy)
            res += max(dx, dy)
            lpx, lpy = points[i]

        return res
        