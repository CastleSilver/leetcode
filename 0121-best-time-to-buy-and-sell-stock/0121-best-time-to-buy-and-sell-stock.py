class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        st = prices[0]
        profit = 0
        for n in range(1, len(prices)):
            if prices[n] - st > profit:
                profit = prices[n] - st
            
            if prices[n] < st:
                st = prices[n]
        
        return profit
            
            