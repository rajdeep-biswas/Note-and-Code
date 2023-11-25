class Solution:
    def rob(self, nums: List[int]) -> int:

        # Foreword: I don't fully understand how this works.
        # I just rewrote some of the code based on intuition from Leetcode/746. Min Cost Climbing Stairs (iterative).py
        # just changing prev2 and prev1 to zero instead of 1st and 0th indices and changing line 12 like so is all it took to make it work for this problem. WTF? What is this sorcery?
        # and of course, line 18 doesn't need a max() anymore.

        robfirst = 0
        dontrobfirst = 0

        for i in range(len(nums)):

            cur = max(nums[i] + robfirst, dontrobfirst)
            robfirst = dontrobfirst
            dontrobfirst = cur
        
        return dontrobfirst