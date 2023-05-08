class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        results = []
        i = 0

        # this majorly uses the solution from Two Sum II (167)
        # sort the array first, take one element at a time as the 'target' variable
        # and apply TwoSumSorted on the rest of the array to find out the remaining two elements that add up to the target
        # do this for each element

        while i < len(sorted_nums):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                i += 1
                continue
            a = sorted_nums[i]
            low = i + 1
            high = len(sorted_nums) - 1

            while low < high:
                if a + sorted_nums[low] + sorted_nums[high] == 0:
                    results.append([sorted_nums[i], sorted_nums[low], sorted_nums[high]])
                    low += 1
                    # some cleverness to avoid entering duplicates into results
                    while sorted_nums[low] == sorted_nums[low - 1] and low < high:
                        low += 1
                elif a + sorted_nums[high] + sorted_nums[low] > 0:
                    high -= 1
                else:
                    low += 1
            i += 1

        return results