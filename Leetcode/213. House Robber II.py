class Solution:
    def rob(self, nums: List[int]) -> int:

        # same thing as Leetcode/198. House Robber.py but do it twice and then get max because you can either include the first element or the last element
        # this was inspired by Babbar's youtube.com/watch?v=Fe2GeXEzWM0. he writes a bit more elegant code in not repeating the same thing but putting it into a method. which is what neetcode has also done, so it's just perfect.

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