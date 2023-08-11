class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0

        # this fantastic solution fetched by chatGPT

        while j < len(nums):

            # i stays at a zero, and j moves until it's found a non-zero and then swaps them
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1