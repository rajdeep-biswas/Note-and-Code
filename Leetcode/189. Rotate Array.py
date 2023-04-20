class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        # the most important step is to do k & length
        # (note that doing this with the non-solution variant makes it work instantly)
        k = k % len(nums)

        # O(n) SPACE solution by taking backup array of k elements
        backup = nums[-k:]

        # iterate through rest elements and shifting them over k indices in a single pass
        i = len(nums) - 1
        while i > k - 1:
            nums[i] = nums[i - k]
            i -= 1

        # place back elements from auxiliary array
        while i >= 0:
            nums[i] = backup[i]
            i -= 1
