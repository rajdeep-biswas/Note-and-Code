class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # final optimization with O(1) space (ignoring the res array)
        res = [1] * len(nums)
        
        # prefix pass
        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        # postfix pass
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res