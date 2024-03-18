class Solution(object):

    # watched neetcode's solution

    def lengthOfLIS(self, nums):
        
        cache = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    cache[i] = max(cache[i], 1 + cache[j])
            
        return max(cache)