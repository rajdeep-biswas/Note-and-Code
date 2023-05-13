class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1

        while r < len(prices):
            # if a smaller value to the right is found just move the purchase decision to that day so you are buying as low as possible
            if prices[r] < prices[l]:
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        return max_profit