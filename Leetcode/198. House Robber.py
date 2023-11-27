class Solution:
    def rob(self, nums: List[int]) -> int:

        # update after an evening of dry running and 2 days of thinking about this problem (see previous commit for older comments that explain my inability to understand)
        # the two variables are meant to keep track of the highest robbed amount til ith and (i - 1)th index

        ith = 0
        iminus1th = 0

        for i in range(len(nums)):

            cur = max(nums[i] + ith, iminus1th)
            ith = iminus1th
            iminus1th = cur
        
        return iminus1th

        """
        
        # for an alternative thought process, think you'd want to make the max() of these two variables, you can actually skip looking at the last index and do the following

        for num in nums[:-1]:
            cur = max(ith + num, iminus1th)
            ith = iminus1th
            iminus1th = cur
        
        # ith + nums[-1] is taking the last calculation into account since we haven't actually looked at that one
        return max(ith + nums[-1], iminus1th)

        """