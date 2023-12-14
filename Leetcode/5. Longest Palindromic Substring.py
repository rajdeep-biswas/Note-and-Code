class Solution:

    # I coded this after a single watch of Neetcode's intuition + solution (youtube.com/watch?v=XYQecbcd6_c)
    # I am very lost on how is this is a dynamic programming solution. There is no memoization or caching, or anything vaguely resembling a DP solution.
    # note: I was using a cur_len = 0 initialization at line 9, then using it to check condition on line 12 instead of (r - l + 1), which is incorrect

    def getLongestPalindrome(self, s, l, r):
        longest = ''

        while l >= 0 and r < len(s) and s[l] == s[r]:

            if (r - l + 1) > len(longest):
                longest = s[l: r + 1]
            
            l -= 1
            r += 1

        return longest

    def longestPalindrome(self, s: str) -> str:

        longest = ''

        for i in range(len(s)):
            
            even = self.getLongestPalindrome(s, i, i + 1)
            if len(even) > len(longest):
                longest = even

            odd = self.getLongestPalindrome(s, i, i)
            if len(odd) > len(longest):
                longest = odd
            
        return longest