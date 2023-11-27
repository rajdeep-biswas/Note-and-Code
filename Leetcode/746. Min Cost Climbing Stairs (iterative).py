class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # very much the same intuition I gained from Leetcode/198. House Robber.py, 
        cost1, cost2 = cost[0], cost[1]

        # just wrote this medium article. https://medium.com/@rajdeepbiswas/hitchhikers-guide-to-dynamic-programming-96afbd4f1c8a. it's 5pm, so left with not enough comments to describe the code here
        for cost in cost[2:]:

            cur = min(cost1, cost2) + cost
            cost1 = cost2
            cost2 = cur
        
        return min(cost1, cost2)