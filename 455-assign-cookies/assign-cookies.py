class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        kid = sorted(g)
        cookie = sorted(s)

        res = 0

        l, r = 0, 0
        while l < len(kid) and r < len(cookie):
            if kid[l] <= cookie[r]:
                l, r = l + 1, r + 1
                res += 1
                continue
            r += 1
        
        return res


        