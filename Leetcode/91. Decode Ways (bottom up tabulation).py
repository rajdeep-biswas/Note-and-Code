class Solution:

    # tabulation technique learned from MrAke's solution on Leetcode Solutions tab

    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0
        
        cache = [0] * (len(s) + 1)
        cache[0] = 1
        cache[1] = 1

        for i in range(2, len(s) + 1):

            charone = s[i - 1]
            chartwo = s[i - 2: i]

            if charone != '0':
                cache[i] += cache[i - 1]
            
            if 10 <= int(chartwo) <= 26:
                cache[i] += cache[i - 2]
            
        return cache[len(s)]