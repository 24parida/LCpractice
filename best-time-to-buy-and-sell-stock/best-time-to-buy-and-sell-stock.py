class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 1
        maxP = 0
        while right < len(prices):
            while prices[right] < prices[left]:
                left = right
                right += 1
                if right >= len(prices):
                    return maxP
            profit = prices[right] - prices[left]
            maxP = max(maxP, profit)
            right += 1
        
        return maxP