class Solution:

    # trying a "reverse fibonacci" approach, as seen on this Babbar video (youtube.com/watch?v=S31W3kohFDk)

    cache = {}

    # going the reverse way, recurrence relation is that of f(n) = f(n + 1) + f(n + 2), and the base case is that of n (cur) reaching "goal"
    def reverseFib(self, goal, cur):
        
        # (2) we check for >= and = goal since the spec specifies we just need to land on n-1th step (0-based index) and not go past it
        if cur >= goal:
            return 1

        if cur in self.cache:
            return self.cache[cur]

        self.cache[cur] = self.reverseFib(goal, cur + 1) + self.reverseFib(goal, cur + 2)

        return self.cache[cur]


    def climbStairs(self, n: int) -> int:

        # it's really strange that I need to clear the cache (because the contents change between testcase to testcase) but for a single testcase it works just fine
        self.cache = {}

        # (1) we pass in n - 1 and not n since it's 0-based indexing
        result = self.reverseFib(n - 1, 0)

        return result