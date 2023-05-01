class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # prefix pass
        pre = 1
        for i in range(len(nums) - 1):
            res[i + 1] *= pre * nums[i]
            pre *= nums[i]

        # postfix pass
        post = 1
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= post * nums[i + 1]
            post *= nums[i + 1]

        return res