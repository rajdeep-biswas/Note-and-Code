class Solution:

    # chatGPT suggested iterative approach

    # we need to initialize some "base cases" into the cache. there's only one way to climb a staircase of length 0 - "to not climb it"
    cache = {0: 1, 1: 1}

    def climbStairs(self, n: int) -> int:
        
        for i in range(2, n + 1):
            self.cache[i] = self.cache[i - 1] + self.cache[i - 2]
        
        return self.cache[n]