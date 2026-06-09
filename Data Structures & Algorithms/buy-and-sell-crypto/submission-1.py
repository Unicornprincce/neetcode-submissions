class Solution:
    def maxProfit(self, prices: List[int]):

        l = 0
        r = 1
        profit = 0

        while r < len(prices):

            if prices[r] < prices[l]:
                l = r
            else:
                if profit < (prices[r] - prices[l]):
                    profit = (prices[r] - prices[l])

            r += 1

        return profit
            