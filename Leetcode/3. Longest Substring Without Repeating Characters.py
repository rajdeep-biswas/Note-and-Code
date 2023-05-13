class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        longest, longer = 0, 0
        l, r = 0, 0
        cur = set()
        while r < len(s):

            if s[r] not in cur:
                longer += 1
                cur.add(s[r])
                r += 1
            else:
                longest = max(longest, longer)
                longer = 0
                cur = set()
                l += 1
                r = l

        longest = max(longest, longer)
        return longest