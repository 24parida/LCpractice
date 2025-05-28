class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        res = 0
        _, prevEnd = intervals[0]
        for start, end in intervals[1:]:
            if start < prevEnd:
                res += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end
        return res
