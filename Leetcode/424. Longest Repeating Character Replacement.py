class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_found = 0
        counts = {}

        # the central improvement in this solution lies in the fact that you don't have to re-iterate over each subsequence to get the counts
        # but you can simply use the sliding window to "update" your counts on the go, since every new l/r movement can only increase (or decrease) the count of only one alphabet at a time
        while r < len(s):
            # this is the delta from my non-solution, update the count dict as you go and decrement it at the else condition
            # we increment at r because that is the pointer that is "discovering" new elements, [1]
            counts[s[r]] = 1 + counts.get(s[r], 0)

            # you still need to find max using O(26)
            max_count = max(counts.values())

            if r - l - max_count < k:
                max_found = max(r - l + 1, max_found)
            else:
                # [1] and we're decrementing at l and then moving it to the right so as to "forget" the element we have moved on from looking at
                counts[s[l]] -= 1
                l += 1

            # this r increment is outside the condition blocks because 1. semantically, we don't need to shrink the window by ONLY moving left since we are not looking to reduce our max_found
            # and also, 2. because moving it within the if condition would plain give wrong results because the r will be counting the r'th character twice. (PS: there can be workarounds by maintaining a last_r value, only if r and that are unequal, count the r'th character, just as a proof of concept - but obviously that is more work than needed)
            r += 1
        
        return max_found