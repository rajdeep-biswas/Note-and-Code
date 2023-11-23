class Solution:

    # from the intuition from this Babbar video (youtube.com/watch?v=S31W3kohFDk)

    cache = dict()

    def solve(self, cost, i):

        # if we've reached either of the first two steps, we just return their cost
        if i <= 1:
            return cost[i]

        if i in self.cache:
            return self.cache[i]
        
        # we're taking the min value of the two possible previous steps added to the current step's cost
        self.cache[i] = min(self.solve(cost, i - 1), self.solve(cost, i - 2)) + cost[i]
        
        return self.cache[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        self.cache = dict()

        # we need yet another min here because the spec states that we can start either from 0th step or the 1st step
        return min(self.solve(cost, len(cost) - 1), self.solve(cost, len(cost) - 2))