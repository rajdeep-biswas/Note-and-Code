class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        # exact same solution as Leetcode/205. Isomorphic Strings.py, which I solved yesterday, check for comments

        map_dict = dict()
        words = s.split(' ')

        # this additional edge case is needed
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):

            if pattern[i] in map_dict and map_dict[pattern[i]] != words[i]:
                return False

            else:
                map_dict[pattern[i]] = words[i]
        
        map_dict = dict()
        words = s.split(' ')

        for i in range(len(words)):

            if words[i] in map_dict and map_dict[words[i]] != pattern[i]:
                return False

            else:
                map_dict[words[i]] = pattern[i]
        
        return True