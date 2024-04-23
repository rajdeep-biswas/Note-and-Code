class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # going to keep track of two values; max_profit_so_far, min_value_so_far

        max_profit_so_far = 0
        min_value_so_far = prices[0]

        for i in range(1, len(prices)):

            # and update each of the two at every step
            # (it's not fully internalized in my brain how this exactly works)
            max_profit_so_far = max(max_profit_so_far, prices[i] - min_value_so_far)
            min_value_so_far = min(min_value_so_far, prices[i])
        
        return max_profit_so_far