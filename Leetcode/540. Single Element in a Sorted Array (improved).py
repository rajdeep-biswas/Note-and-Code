class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # this is an improvement over Leetcode/540. Single Element in a Sorted Array (inelegant).py
        # the major elegance is at the else block line 23 onward
        
        # point left and right for binary search
        l, r = 0, len(nums) - 1
        
        while l <= r:

            # I use two different middle pointers (middle left and middle right) - couldn't come up with a more elegant solution
            m = (l + r) // 2

            # getting booleans for left and right adjacent elements. the sub conditions are for corner cases if we're looking at the 0th or last element (in which case it's true by default)
            left_unmatched = True if m - 1 < 0 else nums[m] != nums[m - 1]
            right_unmatched = True if m + 1 >= len(nums) else nums[m] != nums[m + 1]

            # if both are true, we have found the single-occuring element
            if left_unmatched and right_unmatched:
                return nums[m]
            
            else:

                # neetcode's improvement is here; m (and adjacent index elements) can be used to figure out the size of the left half of the list
                left_size = m - 1 if (m - 1 < 0 or nums[m] == nums[m - 1]) else m # the sub-condition is for handling edge case of m - 1 going out of bounds

                # if the left size is even, we look to the right else we look to the left
                if left_size % 2:
                    r = m - 1
                else:
                    l = m + 1