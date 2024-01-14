class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # attempting naive O(n) solution based on my intuition
        # this finally worked but it takes fucking 8 seconds to beat all testcases on leetcode lmao

        # start looking at first index
        i = 0

        while True:

            # store previous looked at index
            i_prev = i

            # jump to index by adding value at current index
            i += nums[i]
            
            # if we've jumped to or past the last index, that's all we needed to know
            if i >= len(nums) - 1:
                return True

            # if current index value is zero (or has become less than zero because of line 25 from a previous iteration)
            if nums[i] <= 0:

                # we decrement it because we want to check if taking a smaller step would prevent us from landing at a zero
                nums[i_prev] -= 1

                # if the decrement results into a zero, we take a step back to the previous index
                if nums[i_prev] <= 0:
                    i_prev -= 1

                    # if we have walked all the way back to the 0th index, we're doomed
                    if i_prev <= 0:
                        return False

                # ah, after all of this, set i to i_prev so that the latter can keep backing up the value of i
                i = i_prev