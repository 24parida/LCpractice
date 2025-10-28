class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        maxL = []
        for i in height:
            if maxL:
                maxL.append(max(maxL[-1], i))
            else:
                maxL.append(i)

        maxR = []
        for i in height[::-1]:
            if maxR:
                maxR.append(max(maxR[-1], i))
            else:
                maxR.append(i)
        maxR = maxR[::-1]

        res = 0
        for x in range(1, len(height)-1):
            l, r = maxL[x], maxR[x]
            res += max(0, min(l,r) - height[x])
        
        return res
        