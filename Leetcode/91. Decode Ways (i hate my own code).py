class Solution:

    # attempting after watching neetcode's visual explanation and also trying out example decision trees by hand (on my new samsung tab S6 Lite :3)
    # honestly, this solution feels very bodge-y to me personally (as would Tom Scott describe it)
    # but that's probably because it's entirely my own solution uninspired by anyone else's code

    # also the flow / structure of the memoization is heavily inspired by Love Babbar's Coin Change solution Leetcode/322. Coin Change (top down memoized).py

    cache = dict()

    def topDownSearch(self, s, i):

        # memoization
        if i in self.cache:
            return self.cache[i]

        # if i is in bounds, and we find a standalone '0', there will be no value from it. it entirely depends on its predecessor character which is taken care of at the line 31 condition
        if i < len(s) and s[i] == '0':
            return 0

        # "base case" when i goes out of bounds, unbridled by the s[i] == 0 condition above, it means a successful combination has been found
        # note it's important that this "if" occurs *after* the previous one
        if i >= len(s) - 1:
            return 1

        # total can be 0, 1 or 2 depending upon what the recusive calls return. 0 if no decode possible, 1 if the current character is valid, 2 if the pair from the current character is also valid
        total = 0

        total += self.topDownSearch(s, i + 1)
        
        if int(s[i: i + 2]) <= 26:
            total += self.topDownSearch(s, i + 2)

        # memoization
        self.cache[i] = total
        
        return total


    def numDecodings(self, s: str) -> int:
        self.cache = dict()
        return self.topDownSearch(s, 0)