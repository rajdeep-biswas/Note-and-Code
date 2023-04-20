class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # rotate right k times (this takes way too long; 34 / 38 testcases passed)
        for j in range(k):
            temp = nums[-1]
            for i in range(len(nums) - 1, 0, -1):
                nums[i] = nums[i - 1]
            nums[0] = temp