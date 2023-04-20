class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = False

        # set to check if element exists in O(1) time
        hashset = set()
        for num in nums:

            # check if set already has the value, meaning array does contain duplicates
            if num in hashset:
                dup = True
                break

            # if no duplicates yet, just keep adding elements
            hashset.add(num)
        return dup