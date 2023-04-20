class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # dictionary to store each array element and its index
        checks = dict()
        for i in range(len(nums)):

            # find out what is the *other required number* that would complete the required sum
            req = target - nums[i]

            # check if said *other required number* is in the dictionary already, with that, return the current index and the other index
            if req in checks:
                return [i, checks[req]]
            # if not, store current number as key and index as value
            else:
                checks[nums[i]] = i