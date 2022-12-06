class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        # i tried a two pointer approach where one starts from beginning and the other moves backward from the end
        i = 0
        end = len(nums)
        while i < end - 1:
            if nums[i] == nums[i + 1]:

                # poor approach of redundantly copying each element backwards
                # fails one testcase out of 361 testcases due to timeout!
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
                end -= 1
            else:
                i += 1

        return end