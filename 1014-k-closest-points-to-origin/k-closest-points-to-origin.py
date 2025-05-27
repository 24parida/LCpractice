class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            heap.append((dist, x, y))
        heapq.heapify(heap)
        ret = []
        for i in range(k):
            ret.append(heapq.heappop(heap)[1:])
        return ret
        