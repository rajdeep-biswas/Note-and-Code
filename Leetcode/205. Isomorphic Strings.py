class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # map every letter of s to corresponding letter of t
        map_dict = dict()

        for i in range(len(s)):

            # if letter already exists but s:t same index letters are not matching, they're not isomorphic
            if s[i] in map_dict and map_dict[s[i]] != t[i]:
                return False

            # if letter doesn't exist in dict, put it and corresponding letters in
            else:
                map_dict[s[i]] = t[i]
        

        # do the same thing but backwards for t:s. (needed for testcases like s = "badc", t = "baba")
        map_dict = dict()

        for i in range(len(s)):
            if t[i] in map_dict and map_dict[t[i]] != s[i]:
                return False
            else:
                map_dict[t[i]] = s[i]
        
        return True