class Solution:
    def subtract(self, time1, time2) -> int:
        t1h, t1m = time1.split(":")
        t2h, t2m = time2.split(":")
        t1 = int(t1h) * 60 + int(t1m)
        t2 = int(t2h) * 60 + int(t2m)

        h24 = 24 * 60
        diff = abs(t1 - t2)
        wrap_diff = h24 - diff

        return min(diff, wrap_diff)
    
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(set(timePoints)) != len(timePoints):
            return 0

        sorted_times = sorted(timePoints, key = lambda x : int(x.split(":")[0]) * 60 + int(x.split(":")[1]))

        min_diff = float('inf')
        last_time = sorted_times[0]
        for time in sorted_times[1:]:
            diff = self.subtract(time, last_time)
            min_diff = min(min_diff, diff)
            last_time = time

        first, last = sorted_times[0], sorted_times[-1]
        return min(min_diff, self.subtract(last, first))

        
