class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key = lambda x:x[0])
        res = [intervals[0]]
        for it in intervals[1:]:
            if res[-1][-1] >= it[0]:
                res[-1][-1] = max(res[-1][-1], it[-1])
            else:
                res.append(it)
        
        return res
