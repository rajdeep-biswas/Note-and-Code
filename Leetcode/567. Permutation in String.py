class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count_s1 = {}
        for char in s1:
            char_count_s1[char] = 1 + char_count_s1.get(char, 0)
        flag = True
        l, r = 0, len(s1)
        if len(s1) > len(s2):
            return False
        while r < len(s2) + 1:
            flag = True
            char_count_s2 = {}
            for char in s2[l:r]:
                char_count_s2[char] = 1 + char_count_s2.get(char, 0)
            if len(char_count_s1) != len(char_count_s2):
                flag = False
            for char in char_count_s1:
                if char in char_count_s2:
                    if char_count_s1[char] != char_count_s2[char]:
                        flag = False
                else:
                    flag = False
            if flag:
                break
            r += 1
            l += 1
        return flag