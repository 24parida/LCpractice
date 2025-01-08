class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        tickets = deque(tickets)
        while tickets and list[k] != 0:
            tickets[0]-=1
            res += 1
            if tickets[k] == 0:
                return res
            
            k = (k-1) % len(tickets)
            if tickets[0] > 0:
                tickets.append(tickets[0])
            tickets.popleft()


        return res
        