class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        st = prices[length - 1]
        profit = 0
        for n in range(len(prices) - 2, -1, -1):
            if prices[n] < st:
                profit += st - prices[n]
                st = prices[n]
            else:
                st = prices[n]
        
        return profit