class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        res = -1
        l, r = 0, len(height) - 1
        while l<r:
            res = max(min(height[r], height[l]) * (r-l), res)
            if height[l] <= height[r]: l +=1 
            else: r-= 1

        return res