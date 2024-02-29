class Solution:

    # this was neetcode's idea, not mine.
    # i take neither responsibility, nor credit if this fails miserably or works perfectly.
    # okay I do take credit for debugging on my... did I mention my... SAMSUNG GALAXY TAB S6 LITE WITH AN SPEN?

    def maxProduct(self, nums: List[int]) -> int:

        max_prods = [nums[0]]
        min_prods = [nums[0]]

        for i in range(1, len(nums)):
            min_prods.append(min(nums[i], nums[i] * max_prods[i - 1], nums[i] * min_prods[i - 1]))
            max_prods.append(max(nums[i], nums[i] * max_prods[i - 1], nums[i] * min_prods[i - 1]))

        max_prods.extend(min_prods)
        return max(max_prods)