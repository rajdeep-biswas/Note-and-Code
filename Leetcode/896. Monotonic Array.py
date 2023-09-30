class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        # single length should return True
        if len(nums) == 1:
            return True
        
        # my implementation has two variables if both are marked True by the end, then array is not monotonic
        neg = False
        pos = False

        for i in range(len(nums) - 1):

            if nums[i + 1] - nums[i] < 0:
                neg = True
            
            if nums[i + 1] - nums[i] > 0:
                pos = True

            # slight efficiency addition to break out early
            if pos and neg:
                break
        
        # compliment of And - return False only if array has shown increase and decrease (all other cases are monotonic)
        return not(neg and pos)