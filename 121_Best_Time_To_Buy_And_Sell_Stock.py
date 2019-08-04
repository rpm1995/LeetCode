class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        ans = 0

        for price in prices:

            if price < min_price:
                min_price = price
            else:
                ans = max(ans, price - min_price)

        return ans
