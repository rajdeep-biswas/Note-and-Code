class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # i heard neetcode's explanation (youtube.com/watch?v=FPCZsG_AkUg) and implemented this
        # it's the exact same besides he uses n ^ 2 to check at line 13 and i used abs(). also he uses n * n and i use n ** 2

        # with the property of the array, we know the two biggest elements after squaring can only be the first and last elements (since negatives exist), so we use a two pointer approach and compare them and add them to an auxiliary array and converge inwards
        l, r = 0, len(nums) - 1

        res = []

        while l <= r:

            if abs(nums[l]) > abs(nums[r]):
                
                res.append(nums[l] ** 2)
                l += 1

            else:

                res.append(nums[r] ** 2)
                r -= 1
        
        return res[::-1]