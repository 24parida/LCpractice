class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1:0}
        def pow(x):
            if x in memo:
                return memo[x]

            if x%2:
                memo[x] = 1 + pow(3*x+1)
            else:
                memo[x] = 1 + pow(x / 2)
            
            return memo[x]
        
        r = list(range(lo,hi+1))
        r.sort(key = lambda x: (pow(x), x))
        return r[k-1]

        