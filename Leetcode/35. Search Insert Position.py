class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # easy problem with vanilla binary search solution, except*
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        # *this clever little modification of returning l. why does this make sense?
        # well, the left pointer, after the loop exits, will be looking at the index where to insert the target element, sorted (https://www.youtube.com/watch?v=K-RYzDZkzCI, for further explanation)
        return l