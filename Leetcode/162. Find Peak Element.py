class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # inspired by Leetcode/540. Single Element in a Sorted Array (improved).py
        # this is a trash problem because we don't really need to return the highest existing peak but any peak at all that we find first
        # take the custom testcase [10,2,1,3,5,6,4]

        l, r = 0, len(nums) - 1

        while l <= r:

            m = (r + l) // 2
            
            # I sort of used the intuition from Leetcode/11. Container With Most Water.py; keep looking at the higher element
            left_matched = m - 1 < 0 or nums[m] > nums[m - 1]
            right_matched = m + 1 >= len(nums) or nums[m] > nums[m + 1]

            if left_matched and right_matched:
                return m
            
            else:

                # move pointer towards the half of the array that contains the higher peak
                if nums[m] < nums[m + 1]:
                    l = m + 1
                else:
                    r = m - 1 