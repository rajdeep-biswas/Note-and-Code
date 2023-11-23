class Solution:

    # trying a "reverse fibonacci" approach, from the intuition from this Babbar video (youtube.com/watch?v=S31W3kohFDk); he doesn't show the code
    # using the code in Leetcode/509. Fibonacci Number (cached).py 1:1 will work just fine, I just tried to do a more "climbing staircase"-analogous solution by going from 0 to nth
    # the caching mechanism isn't very intuitive in this one, and works in a reversed way - cache[0] will have the final answer, also -
    # it's kinda very inefficient compared to the standard approach - takes way more total calls (although number of cache hits also increase when n is large but that's like a solution to a problem that it itself has created)

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