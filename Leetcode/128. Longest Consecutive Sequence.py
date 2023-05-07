class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        nums = list(nums_set)

        # this is the optimized solution
        # use set to make the lookup time O(1)

        longest = 1
        i = 0
        while i < len(nums):
            length = 1
            # check if current element has a predecessor, if not, it is potentially the start of a fresh subsequencs
            if nums[i] - 1 not in nums_set:

                # check if there are further elements in said sequence and keep updating the length
                while nums[i] + length in nums_set:
                    length += 1
            longest = max(longest, length)
            i += 1

        return longest