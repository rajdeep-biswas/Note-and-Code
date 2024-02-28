class Solution:

    # my slightly modified take on love babbar's non-memoized solution with memoization
    # source: https://www.youtube.com/watch?v=A3FHNCAkhxE&t=31s

    cache = dict()

    def bfs(self, coins, target):

        # if subtracted amount (target minus coin) has reached zero, we have found a solution
        if target == 0:
            return 0
        
        # if subtracted amount (target minus coin) has reached lower than zero, this is an invalid path
        if target < 0:
            return -1

        # if target already exists in cache, return value
        if target in self.cache:
            return self.cache[target]
        

        # looking for the smallest possibility at current level with all possible coins
        mini = float('inf')

        for coin in coins:

            # to get the "answer", we need to recursively look for all coin possibilities as well
            ans = self.bfs(coins, target - coin)

            # if answer is zero or some value, we update "mini"mum found
            if ans != -1:
                mini = min(mini, 1 + ans)
        
        # we store smallest found value in cache for memoization
        self.cache[target] = mini

        return mini

    def coinChange(self, coins: List[int], amount: int) -> int:

        self.cache = dict()
        ans = self.bfs(coins, amount)
        if ans == float('inf'):
            return -1
        return ans