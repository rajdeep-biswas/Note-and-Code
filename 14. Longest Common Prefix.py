class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        base = strs[0]
        longest = ''
        for i in range(len(base)):
            found = True
            for st in strs[1:]:
                if i >= len(st) or st[i] != base[i]:
                    found = False
            if found:
                longest += base[i]
            else:
                break
        return longest