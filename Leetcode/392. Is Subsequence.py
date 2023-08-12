class Solution:
    # Easy problem but it used to appear intimidating to me first, so I like my instant solution
    def isSubsequence(self, s: str, t: str) -> bool:
        idxs = 0
        idxt = 0
        count = 0
        
        while idxs < len(s) and idxt < len(t):
            if s[idxs] == t[idxt]:
                count += 1
                idxs += 1
            idxt += 1

        return count == len(s)