class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # we run the loop as long as left does not cross right
        while l <= r:
        
            m = (l + r) // 2
                
            if nums[m] == target:
                return m
            
            # if m is in the left-sorted half of the array
            if nums[m] >= nums[l]:
                
                # if target element is to the left of leftmost or to the right of mid
                if target < nums[l] or target > nums[m]:
                    # then we eliminate left half of the array
                    l = m + 1
                else:
                    # we eliminate right half of the array
                    r = m - 1
            
            # if m is in the right-sorted half of the array
            else:

                # if target element is to the right of rightmost or to the left of mid
                if target > nums[r] or target < nums[m]:
                    # then we eliminate right half
                    r = m - 1
                else:
                    l = m + 1

        return -1
