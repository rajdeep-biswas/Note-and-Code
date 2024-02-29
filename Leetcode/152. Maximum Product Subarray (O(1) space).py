class Solution:

    # this was neetcode's idea, not mine.
    
    def maxProduct(self, nums: List[int]) -> int:

        global_max = nums[0]
        max_prod = nums[0]
        min_prod = nums[0]

        for i in range(1, len(nums)):
            temp = min_prod

            # key is to understand that all decisions have to be taken based on three values;
            # current index by itself, current index multiplied to previous max, and current index multiplied to previous min
            # (there is no way to solve this without taking all three options into consideration)
            min_prod = min(nums[i], nums[i] * max_prod, nums[i] * min_prod)
            max_prod = max(nums[i], nums[i] * max_prod, nums[i] * temp)
            global_max = max(global_max, max_prod)

        return global_max
