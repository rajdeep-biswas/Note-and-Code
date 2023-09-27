class Solution:

    # this is a recursive version of neetcode's solution. i have also identified that we don't need max(m, res) at line 21; just passing m in place of res works
    # tweaked binary search with the < and = conditions combined into one
    def binarySearch(self, have, l, r, res):

        # base case returns res instead of -1 because we can always create a staircase of size 1 (since it's constrained by the problem)
        if l > r:
            return res
        
        # looking at mid, the potential "highest" staircase size that we're attempting. since clearly we can't make n size staircase with n coins
        m = (l + r) // 2

        # to make a staircase of size m, we will need sum(1:m) coins
        will_need = m * (m + 1) // 2

        # checking if we have that many coins (n)
        if will_need <= have:

            # if we already possess that many coins, we can look higher, we change the result to be m, since there's no need to go back now. rest is standard binary search parameter change
            return self.binarySearch(have, m + 1, r, m)
        
        # if we don't have enough coins, we look lower
        else:
            # standard binary search parameter change
            return self.binarySearch(have, l, m - 1, res)
        

    def arrangeCoins(self, n: int) -> int:

        # res is set to 1 initially because we're trying to find max; we can, however don't need to, set it to 0 since the problem constraints state that n will be at least 1

        # have n coins, left is 1, right is n, result is "at least" 1
        return self.binarySearch(n, 1, n, 1)