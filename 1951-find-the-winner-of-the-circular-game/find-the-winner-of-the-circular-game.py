class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = collections.deque(list(range(1, n+1)))

        c = 0
        while len(q) != 1:
            person = q.popleft()
            c = (c + 1) % k
            if c != 0:
                q.append(person)
                    
        return q[0]
