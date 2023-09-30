class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        # I got the intuition from neetcode's video (youtube.com/watch?v=HGtqdzyUJ3k) and coded my own implementation (it's a bit inelegant but it works).
        # idea: the list will always be originally odd-sized because all numbers occur in pairs besides one. once you've looked at the center, you need to account for one adjacent element and then divide and conquer towards the half of the array which continues to have odd elements (since the half that has even elements is already paired up) - again, watch the video if this does not make sense.
        
        # point left and right for binary search
        l, r = 0, len(nums) - 1
        
        while l <= r:

            # I use two different middle pointers (middle left and middle right) - couldn't come up with a more elegant solution
            ml = (l + r) // 2

            # getting booleans for left and right adjacent elements. the sub conditions are for corner cases if we're looking at the 0th or last element (in which case it's true by default)
            left_unmatched = True if ml - 1 < 0 else nums[ml] != nums[ml - 1]
            right_unmatched = True if ml + 1 >= len(nums) else nums[ml] != nums[ml + 1]

            # if both are true, we have found the single-occuring element
            if left_unmatched and right_unmatched:     
                return nums[ml]
            
            else:

                # if not, we check if it matches the left or right adjacent element
                if nums[ml] == nums[ml - 1]:
                    mr = ml - 1
                
                else:
                    mr = ml + 1
                
                # semantic rearrangement, for consistency, that ml should occur to the left of mr
                if ml > mr:
                    ml, mr = mr, ml
                
                # if the right half is odd, binary search to the left (checking for left half also being even is redundant)
                if (r - mr) % 2:
                    l = mr + 1
                else:
                    r = ml - 1