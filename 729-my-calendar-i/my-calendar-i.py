import bisect
class MyCalendar:

    def __init__(self):
        self.times = []

    def book(self, startTime: int, endTime: int) -> bool:
        l, r = 0, len(self.times) - 1   
        while l <= r:
            mid = (l + r) // 2
            if self.times[mid][0] <= startTime:
                l = mid + 1
            else:
                r = mid - 1
        
        overlaps_end_prev = l > 0 and startTime < self.times[l-1][1]
        overlaps_start_next = l < len(self.times) and endTime > self.times[l][0]

        if overlaps_end_prev or overlaps_start_next:
            return False
        else:
            self.times.insert(l, (startTime, endTime))
            return True 

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)