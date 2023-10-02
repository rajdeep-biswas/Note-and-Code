class Solution:
    def findMin(self, nums: List[int]) -> int:

        # inspired from neetcode (youtube.com/watch?v=nIVW4P8b1VA)
        # his solution is also inelegant in its own way so i am happy with my solution for now
        # edge case of array size being 1 (this is the only inelegant part of the code I personally don't like)
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        # this handles the corner case if the array is not rotated (regular sorted array)
        if nums[l] < nums[r]:
            return nums[l]

        # tweaked binary search
        while l < r:

            m = (l + r) // 2

            # if the element to the right of middle is greater than the middle, we have found our "pivot" and hence our answer
            if nums[m + 1] < nums[m]:
                return nums[m + 1]
            
            # identify if middle is part of the "right sorted half" of the array (check neetcode's video explanation if this is not making sense)
            if nums[m] > nums[l]:
                l = m
            
            # or the "left sorted half"
            else:
                r = m