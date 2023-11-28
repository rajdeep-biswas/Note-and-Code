class Solution:
    def rob(self, nums: List[int]) -> int:

        # update after an evening of dry running and 2 days of thinking about this problem (see previous commit for older comments that explain my inability to understand)
        # the two variables are meant to keep track of the highest robbed amount til iminus1th and (i - 1)th index

        """
        think of the most simple problem, just two houses; [1,2]
        ith is meant to keep track of max money fetchable at index 0 (which is 1), and iminus1th does the same for index before ith (which is index 1 with value 1), so as to not forget about the branching progress made so far.
        as i goes through the array, an additional variable is needed to make a minmaxing decision involving these two variables AND the current position.
        in this case, the decision is to maximize the loot from either the current house plus the last-to-last house OR the last house only, since we cannot rob two in a row.
        before starting, we keep both to 0
        
        taking the example of [1, 2, 3, 1], consider the below dry run -
        at i = 0, the max so far is 1. we keep 
        at i = 1, the max so far is 2

        1. nums[2:] not working with this one because 746 has a minimum constraint of array size
        2. about initialization, you initialize both this and 746 problem variables with 0s some trickiness, house robber can be cleverly be initialized with -
        
        iminus1th = nums[0]
        ith = max(nums[0], nums[1])
        
        but will require a testcase of
        
        if len(nums) < 3:
            return max(nums)

        Learned so much this afternoon, I have covered all of this and more better in this medium article (my first ever!): https://medium.com/@rajdeepbiswas/hitchhikers-guide-to-dynamic-programming-96afbd4f1c8a.
        """
        iminus1th = 0
        ith = 0

        for i in range(len(nums)):

            cur = max(nums[i] + iminus1th, ith)
            iminus1th = ith
            ith = cur

        return ith

        """

        # for an alternative thought process, think you'd want to make the max() of these two variables, you can actually skip looking at the last index and do the following

        for num in nums[:-1]:
            cur = max(iminus1th + num, ith)
            iminus1th = ith
            ith = cur

        # iminus1th + nums[-1] is taking the last calculation into account since we haven't actually looked at that one
        return max(iminus1th + nums[-1], ith)

        PS: Babbar's solution to a different problem is where I got the intuition from youtube.com/watch?v=m9-H6AUBLgY

        """