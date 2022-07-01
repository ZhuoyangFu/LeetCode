class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0

        low = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            profit = max(profit, prices[i] - low)

        return profit