class Solution:
    def isPalindrome(self, s: str) -> bool:

        # O(1) space improvement

        s = s.lower()
        l, r = 0, len(s) - 1

        while l < r:

            # roll left pointer to the right until an alphanumeric character is encountered
            while not s[l].isalnum():
                l += 1

                # this check is needed to make sure if l runs all the way through the string and finds no alphanumeric character, by spec, it should return True and not False
                if l >= len(s):
                    return True

            # roll right pointer to the left until an alphanumeric character is encountered
            while not s[r].isalnum():
                r -= 1

            # compare left and right indices, if a single mismatch is found, it's not palindrome
            if s[l] != s[r]:
                return False

            # proceed to next characters for each
            l += 1
            r -= 1

        # if no mismatches are found, string must be palindromic
        return True