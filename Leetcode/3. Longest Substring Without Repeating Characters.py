class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):

            # while the rightmost found character exists as a duplicate in the set, keep removing from the left until it's removed.
            # note that all elements to the left of the duplicate character will have to be removed in order to preserve the "subsequence-ness"
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            # this will take care of both cases of adding newly found character and adding back the duplicate character after all (one) occurence has been removed
            char_set.add(s[r])

            # set res to the gap between r and l
            res = max(res, r - l + 1)

        return res