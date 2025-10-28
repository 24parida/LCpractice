class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        heapa = []
        heapb = []
        cost = 0


        for a, b in costs:
            if a <= b:
                heapa.append(b - a)
                cost += a
            else:
                heapb.append(a - b)
                cost += b

        heapq.heapify(heapa)
        heapq.heapify(heapb)

        countA, countB = len(heapa), len(heapb)

        if countA == countB:
            return cost
        
        if countA > countB:
            for _ in range((countA - countB) // 2):
                cost += heapq.heappop(heapa)
        else:
            for _ in range((countB - countA) // 2):
                cost += heapq.heappop(heapb)
        
        return cost
