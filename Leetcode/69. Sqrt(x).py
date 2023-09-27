class Solution:
    def mySqrt(self, num: int) -> int:

        # exact same solution as #376, just had to change the return values

        l, r = 1, num

        while l <= r:

            m = (l + r) // 2

            if m ** 2 > num:
                r = m - 1
            
            elif m ** 2 < num:
                l = m + 1
            
            else:
                return m
        
        return l - 1