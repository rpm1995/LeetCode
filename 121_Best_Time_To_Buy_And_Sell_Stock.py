class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        ans = 0
        lowest = prices[0]

        for i in range(len(prices)):

            price = prices[i]

            if price > lowest:
                ans = max(ans, price - lowest)
            else:
                lowest = price

        return ans
