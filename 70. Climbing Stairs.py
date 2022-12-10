class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:

        # combining DP with recursion, do remember to put the base case ABOVE the caching condition
        if n <= 1:
            return 1

        # if result is not in cache, compute using recursion (which you'd normally directly return)
        if n not in self.cache:
            self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # and then actually return using cache, and not another computation
        return self.cache[n]