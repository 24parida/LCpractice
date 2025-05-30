class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 0:
            return [[]]

        intervals = sorted(intervals, key = lambda i : i[0])

        res = [intervals[0]]
        for start, end in intervals[1:]:
            top_int = res[-1]
            if top_int[1] >= start:
                new_int = [min(top_int[0], start), max(top_int[1], end)]
                res[-1] = new_int
            else:
                res.append([start, end])
        return res

        