class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # solution inspired by Babbar's solve3() youtube.com/watch?v=S31W3kohFDk
        # this is probably where Neetcode's solution was coming from (except he goes the extra step of not even using two extra variables but overwriting values into the input array. absolute madlad)
        
        prev2 = cost[0]
        prev1 = cost[1]

        for i in range(2, len(cost)):

            cur = cost[i] + min(prev2, prev1)
            prev2 = prev1
            prev1 = cur
        
        return min(prev2, prev1)