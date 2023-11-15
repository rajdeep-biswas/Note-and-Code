class Solution:
    
    # was watching Love Babbar's intro to DP (youtube.com/watch?v=PGsgv6nXhLw&) and I got this idea of -
    # initializing base cases into cache instead of writing them into the recursion base case/s
    cache = {0: 0, 1: 1}

    def fib(self, n: int) -> int:

        # instead of n == 1 or 0, return n
        if n in self.cache:
            return self.cache[n]

        # generate cache at every step
        self.cache[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.cache[n]