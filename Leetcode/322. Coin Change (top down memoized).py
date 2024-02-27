class Solution:

    # my slightly modified take on love babbar's non-memoized solution with memoization
    # source: https://www.youtube.com/watch?v=A3FHNCAkhxE&t=31s

    cache = dict()

    def bfs(self, coins, target):

        if target == 0:
            return 0
        
        if target < 0:
            return -1

        if target in self.cache:
            return self.cache[target]
        
        mini = float('inf')

        for coin in coins:
            
            ans = self.bfs(coins, target - coin)

            if ans != -1:
                mini = min(mini, 1 + ans)
        
        self.cache[target] = mini

        return mini

    def coinChange(self, coins: List[int], amount: int) -> int:

        self.cache = dict()
        ans = self.bfs(coins, amount)
        if ans == float('inf'):
            return -1
        return ans