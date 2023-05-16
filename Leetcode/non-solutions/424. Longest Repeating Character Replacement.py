class Solution:

    # caffeine crashed implementation of what I understood the neetcode guy was talking about. 27/38 testcases, timeouts on rest.

    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_found = 0
        while r < len(s):

            # move sliding window starting from 0, 0 and get highest occuring frequency
            counts = {}
            for i in range(l, r + 1):
                counts[s[i]] = 1 + counts.get(s[i], 0)
            max_count = max(counts.values())

            # print(l, r, s[l:r + 1], max_count, k, r - l - max_count < k, counts)

            # if current window has fewer than k elements to replace discounting the highest frequency element, check if current window length is higher than max_found, else move left pointer
            if r - l - max_count < k:
                max_found = max(r - l + 1, max_found)
            else:
                l += 1
            r += 1
        
        return max_found