class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(i):
            print(curr)
            if (len(curr) == k):
                res.append(curr.copy())
                return
            for x in range(i, n+1):
                curr.append(x)
                backtrack(x+1)
                curr.pop()
        
        backtrack(1)
        return res