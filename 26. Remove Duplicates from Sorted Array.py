class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i = j = 1

        # Diptesh da's two-pointer / slow-and-fast pointer approach that removes my redundancy of copying each element backwards each time a duplicate is found
        while i < len(nums):

            # this part makes sure a copy is made directly from the next-found-unique element instead of copying each one-by-one
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
            i += 1

        return j