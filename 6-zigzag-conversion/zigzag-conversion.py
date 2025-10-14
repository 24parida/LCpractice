class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        res = [[] for _ in range(numRows)]
        i = 0
        cur = 1
        for j in s:
            res[i].append(j)
            if i == numRows - 1:
                cur = -1
            if i == 0:
                cur = 1
            i += cur

        ans = ["".join(i) for i in res]
        return "".join(ans)
        