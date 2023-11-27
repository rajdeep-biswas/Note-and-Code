class Solution:

    cache = {}
    def tribonacci(self, n: int) -> int:

        # been in the flow of DP today (just published first medium article this afternoon)
        # just shoved in a bunch of base cases based on observation.

        if n <= 1:
            return n
        if n <= 3:
            return n - 1

        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        return self.cache[n]