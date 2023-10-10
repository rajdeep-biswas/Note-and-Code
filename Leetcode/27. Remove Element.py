class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # completed a half done chatGPT suggestion and redid it from scratch

        i, k = 0, 0

        # keep k at the lowest index until it doesn't have val anymore.
        while i < len(nums):
            if nums[i] != val:

                # swap out any other element with val
                nums[i], nums[k] = nums[k], nums[i]

                # once array has no val until k element, push k to the right
                k += 1

            i += 1

        # spec asks k to be returned. array has all vals moved to the right of k
        return k