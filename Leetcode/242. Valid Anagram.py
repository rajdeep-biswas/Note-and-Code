class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        """
        Note that a good engineering practice is the check up here if the lengths of the two strings match.
        In the case that the lengths do not match, it can be safe to return False right here without going into further computation.
        """

        # maintain dictionaries for checking letter count in each string
        count_1, count_2 = {}, {}

        # get frequency of letters in each string
        for i in range(len(s)):
            count_1[s[i]] = 1 + count_1.get(s[i], 0)
            count_2[t[i]] = 1 + count_2.get(t[i], 0)

        # pythonic way to check if two dictionaries are the exact same and simply return the boolean value from the equals operator
        return count_1 == count_2