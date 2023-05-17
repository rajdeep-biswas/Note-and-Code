class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_found = 0
        counts = {}

        while r < len(s):
            # this is the delta from my non-solution, update the count dict as you go and decrement it at the else condition
            counts[s[r]] = 1 + counts.get(s[r], 0)

            # you still need to find max using O(26)
            max_count = max(counts.values())

            if r - l - max_count < k:
                max_found = max(r - l + 1, max_found)
            else:
                counts[s[l]] -= 1
                l += 1
            r += 1
        
        return max_found