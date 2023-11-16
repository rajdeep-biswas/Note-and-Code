class Solution:

    # trying a "reverse fibonacci" approach, as seen on this Babbar video (youtube.com/watch?v=S31W3kohFDk)

    # going the reverse way, recurrence relation is that of f(n) = f(n + 1) + f(n + 2), and the base case is that of n (cur) reaching "goal"
    def reverseFib(self, goal, cur):
        
        # (2) we check for >= and = goal since the spec specifies we just need to land on n-1th step (0-based index) and not go past it
        if cur >= goal:
            return 1

        return self.reverseFib(goal, cur + 1) + self.reverseFib(goal, cur + 2)


    def climbStairs(self, n: int) -> int:

        # (1) we pass in n - 1 and not n since it's 0-based indexing
        return self.reverseFib(n - 1, 0)
    
    # PS: this solution, without caching, gives a TLE. the caching mechanism isn't as straightforward as Fibonacci. just keeping this in non-solutions for now.