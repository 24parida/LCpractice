class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = [] 
        def combinations(i): 
            if len(sol) == k: 
                res.append(sol[:]) 
                return 
            for x in range(i, n + 1): 
                sol.append(x)
                combinations(x+1)
                sol.pop()

        combinations(1)
        return res