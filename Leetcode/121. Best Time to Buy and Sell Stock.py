class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # https://www.youtube.com/watch?v=excAOvwF_Wk
        max_profit = 0
        min_ = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_)
            min_ = min(min_, prices[i])

        return max_profit