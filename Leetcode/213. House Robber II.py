class Solution:
    def rob(self, nums: List[int]) -> int:

        # same thing as Leetcode/198. House Robber.py but do it twice and then get max because you can either include the first element or the last element

        if len(nums) == 1:
            return nums[0]

        a, b = 0, 0

        for num in nums[:-1]:
            temp = max(a + num, b)
            a = b
            b = temp
        
        maxa = b

        a, b = 0, 0
        
        for num in nums[1:]:
            temp = max(a + num, b)
            a = b
            b = temp
        
        maxb = b
        
        return max(maxa, maxb)