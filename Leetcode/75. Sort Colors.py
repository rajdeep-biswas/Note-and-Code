class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # we need three pointers; one for iterating element by element. other two keep tracks of 0s at the beginning of the array and 2s at end of the array; the remaining 1s get sorted in-place, being the only remaining elements

        i, left, right = 0, 0, len(nums) - 1

        while i <= right: # <= because we've set right to len(nums) - 1

            # dry running this is the best way to understand what is happening
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
            
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                i -= 1 # without this, testcases like [1, 2, 0] will fail because i surpasses right after the first swap [1 0 2] and the (1, 0) never get compared
            
            i += 1

        """
        neetcode's video explanation wasn't making much sense to me. leetcode/timkillis's discussion thread however resonated with me (context: read the story in  Leetcode/non-solutions/75. Sort Colors (interesting story).py) and I coded that up. Just in case it's gone missing by the time you're reading this, I'm pasting his comment below here -

        timkillis | Feb 10, 2019
        I had a hard time grasping this one so I thought I'd write it down, maybe it will help you too.

        Iterate over the array, maintaining two pointers, one at the "low" index, 0, and one at the "high", nums.length - 1.

        Everything to the left of low in the array and everything to the right of high in the array will be assumed sorted. As we iterate through the array, we update our pointers, taking account for two cases

        If the index in the array is equal to 0, we swap that with our current low index and then increment the low index, since we know that everything to the left of that index is properly sorted.

        Else if the index in the array is equal to 2, we swap that with our current high index and decrement the high index, since everything to right of the high index is sorted. Also take care in this case to decrement i since we will want to reconsider the inserted element.

        We've accounted for if the indexes are 0 or 2, the only other option is if the index is a 1, in which case we will just leave it in place.

        """