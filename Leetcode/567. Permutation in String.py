class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # i will try my best to explain the thought process
        # update: turns out it's actually pretty close to neetcode's O(26.n) solution, so I am gonna keep this one for now and not upgrade to the _slight_ improvement

        # sanity check
        if len(s1) > len(s2):
            return False

        char_count_s1 = {}

        # get frequencies of characters of the first string
        for char in s1:
            char_count_s1[char] = 1 + char_count_s1.get(char, 0)
        flag = True
        l, r = 0, len(s1)

        while r < len(s2) + 1:
            # assume flag to be true every iteration
            flag = True

            # get charater frequency of second string but only from l to r, which is the window length based on the first string
            char_count_s2 = {}
            for i in range(l, r):
                char_count_s2[s2[i]] = 1 + char_count_s2.get(s2[i], 0)

            # sanity check
            if len(char_count_s1) != len(char_count_s2):
                flag = False

            # check if both frequencies are same
            for char in char_count_s1:
                if char in char_count_s2:
                    if char_count_s1[char] != char_count_s2[char]:
                        flag = False
                else:
                    flag = False

            # check if still true, finding at least one instance is good enough so we can break
            if flag:
                break

            # if not found slide window to the left by one
            r += 1
            l += 1

        return flag