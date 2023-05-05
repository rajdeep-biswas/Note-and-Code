class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # i am not allowed to sort but I was just PoC'ing the rest of the solution.
        # which only worked once I introduced `set` to remove duplicates
        nums = sorted(set(nums))
        subseq_lengths = []
        longest = 1
        # print(nums)
        for i in range(1, len(nums)):
            print(nums[i - 1] + 1, nums[i])
            if nums[i - 1] + 1 == nums[i]:
                longest += 1
            else:
                subseq_lengths.append(longest)
                longest = 1
        subseq_lengths.append(longest)
        return max(subseq_lengths)