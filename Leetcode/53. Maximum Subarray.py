class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # as explained by neetcode youtube.com/watch?v=5WZl3MMT0Eg

        max_sum = nums[0]
        cur_sum = 0

        for num in nums:

            # this keeps the cur_sum from contributing to the max by "moving the left pointer" to the right, if it has gone below zero (i.e. via a negative number getting added to the cur_sum)
            cur_sum = max(cur_sum, 0)
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
        
        return max_sum