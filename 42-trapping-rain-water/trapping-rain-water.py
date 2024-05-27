class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        minL = [0] * len(height)
        minR = [0] * len(height)
        res = 0

        for x, i in enumerate(height):
            if x==0: minL[0] = i
            else: minL[x] = max(minL[x-1], i)

        for i in range(len(height)-1,-1,-1):
            if i==(len(height)-1): minR[len(height)-1] = height[i]
            else: minR[i] = max(minR[i+1], height[i])

        temp = [0] * len(height)
        for i in range(1, len(height) - 1):
            res += max(min(minL[i-1], minR[i+1]) - height[i], 0)
            temp[i] = min(minL[i-1], minR[i+1]) - height[i]

        return res