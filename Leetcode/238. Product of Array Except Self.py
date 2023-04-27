class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # my initial solution of computing total_product of array and just dividing by index location's number, and when the number is 0, just recalculating for that index
        # pretty proud of it, but also sure it can be improved
        total_prod = 1
        for num in nums:
            total_prod *= num
        res = []
        for i in range(len(nums)):
            if nums[i]:
                res.append(total_prod // nums[i])
            else:
                mult = 1
                for j in range(len(nums)):
                    if i != j:
                        mult *= nums[j]
                res.append(mult)
        return res