class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        idx = 0

        for it in intervals:
            if it[0] >= newInterval[0]:
                break
            
            res.append(it)
            idx += 1
        
        if len(res) == 0 or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1][1] = max(newInterval[1], res[-1][1])
        

        for it in intervals[idx:]:
            if res[-1][1] >= it[0]:
                res[-1][1] = max(res[-1][1], it[1])
            else:
                res.append(it)
                
        return res


        

        