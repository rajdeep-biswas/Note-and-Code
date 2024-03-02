class Solution:

    # replicating bottom-up solution as coded by babbar
    # also, turns out it's the exact same solution as Neetcode's

    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = [float("inf")] * (amount + 1)
        cache[0] = 0

        # for every single "whole number" values that are counting up to amount
        for i in range(1, amount + 1):

            # for all coins
            for coin in coins:

                if i - coin >= 0:
                    cache[i] = min(cache[i], 1 + cache[i - coin])

        if cache[amount] == float('inf'):
            return -1
        return cache[amount]