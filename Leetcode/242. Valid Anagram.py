class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # maintain dictionaries for checking letter count in each string
        count_1 = {}
        count_2 = {}

        # count frequency of letters in string 1
        for letter in s:
            if letter in count_1:
                count_1[letter] += 1
            else:
                count_1[letter] = 1

        # count frequency of letters in string 2
        for letter in t:
            if letter in count_2:
                count_2[letter] += 1
            else:
                count_2[letter] = 1

        # pythonic way to check if two dictionaries are the exact same and simply return the boolean value from the equals operator
        return count_1 == count_2