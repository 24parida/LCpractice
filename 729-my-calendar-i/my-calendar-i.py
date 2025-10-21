class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.start = None
        self.end = None

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = Node()
            self.root.start = startTime
            self.root.end = endTime
            return True

        prev = None
        curr = self.root
        while curr:
            if endTime <= curr.start:
                prev = curr
                curr = curr.left
            elif startTime >= curr.end:
                prev = curr
                curr = curr.right 
            else:
                return False
            
        if endTime <= prev.start:
            prev.left = Node()
            prev.left.start = startTime
            prev.left.end = endTime
        elif startTime >= prev.end:
            prev.right = Node()
            prev.right.start = startTime
            prev.right.end = endTime
        return True

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)