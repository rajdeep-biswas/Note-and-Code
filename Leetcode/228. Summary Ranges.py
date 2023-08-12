class Solution:

    # Easy problem but the solution was quite involved
    def summaryRanges(self, nums: List[int]) -> List[str]:

        # sanity
        if not nums:
            return nums

        # initiating first to nums[0] since that doesn't require a check, it will never have to be None.
        # last, on the other hand is explained below, why it may be None
        ranges = []
        first, last = nums[0], None

        for i in range(1, len(nums)):

            # if the current index still "in range" i.e incremented by one compared to last, according to the problem, update "last" to it
            if nums[i] == nums[i - 1] + 1:
                last = nums[i]

            # if you have found a non-consecutive element, that means you have found your previous range
            else:

                # now there are two cases,
                # you may have found a second number that does in fact make your a range a pair of numbers
                if last != None:
                    ranges.append(str(first) + "->" + str(last))

                # or you may only have one number without an accompanying number, so it's a range in itself
                # the two example testcases really help drive the point home. leetcode.com/problems/summary-ranges
                else:
                    ranges.append(str(first))

                # resetting to the same statement as on line 13
                first, last = nums[i], None

        # repeating the if-else condition as was within the loop to account for any remaining "Last" value
        # note, this is the exact same conditional as on line 26, just rewritten into a single line
        ranges.append(str(first) + ("->" + str(last) if last else ''))

        return ranges