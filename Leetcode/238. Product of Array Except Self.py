class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(n) improvement with neetcode guy's suggestion on using two different arrays
        # the space complexity of this can indeed be further improved, he also said (https://www.youtube.com/watch?v=bNvIQI2wAjk)
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        
        for i in range(len(nums)):
            prefix[i] = (prefix[i - 1] if i > 0 else 1) * nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = (postfix[i + 1] if i < len(nums) - 1 else 1) * nums[i]

        for i in range(len(nums)):
            nums[i] = (prefix[i - 1] if i > 0 else 1) * (postfix[i + 1] if i < len(nums) - 1 else 1)

        return nums