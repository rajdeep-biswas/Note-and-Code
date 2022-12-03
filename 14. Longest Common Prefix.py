class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # using the first string as a base since the longest possible common prefix cannot be longer than the shortest string!
        base = strs[0]
        longest = ''

        # iterating through each letter
        for i in range(len(base)):
            found = True

            # checking if said letter occurs at each the desired index for each string (besides the first one)
            for st in strs[1:]:

                # checking each string shouldn't go beyond it's actual length in order to avoid a out of bounds index.
                if i >= len(st) or st[i] != base[i]:
                    found = False

            if found:
                longest += base[i]
            else:
                # if even one match fails, it's incorrect to keep looking further, let alone inefficient!
                break
        return longest