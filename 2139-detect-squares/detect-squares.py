class DetectSquares:

    def __init__(self):
        self.g = collections.defaultdict(lambda: collections.defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.g[x][y] += 1
        
    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        for y2 in self.g[x]:
            r = abs(y2 - y)
            if r == 0:
                continue
            x2 = x - r
            count += self.g[x][y2] * self.g[x2][y2] * self.g[x2][y]
            x2 = x + r
            count += self.g[x][y2] * self.g[x2][y2] * self.g[x2][y]
        return count
            
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)