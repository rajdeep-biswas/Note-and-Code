class Solution:

    # my take on neetcode's solution. feels a bit too builtin-y

    def compare(self, num1, num2):

        if num1 + num2 < num2 + num1:
            return 1
        return -1

    def largestNumber(self, nums: List[int]) -> str:
        
        # convert integers to strings for easier comparison
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        # use custom sorting method
        nums.sort(key = cmp_to_key(self.compare))

        return str(int("".join(nums)))