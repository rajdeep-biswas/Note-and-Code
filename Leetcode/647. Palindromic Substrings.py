class Solution:

    # pretty much the same solution as Leetcode/5. Longest Palindromic Substring.py
    # also happy to announce that is the exact same (a bit more readable) solution as Neetcode's

    def countPalindromes(self, s, l, r):
        count = 0

        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            r += 1
            l -= 1

        return count

    def countSubstrings(self, s: str) -> int:

        odd_counts, even_counts = 0, 0
        
        for i in range(len(s)):

            odd_counts += self.countPalindromes(s, i, i)
            even_counts += self.countPalindromes(s, i, i + 1)
        
        return odd_counts + even_counts