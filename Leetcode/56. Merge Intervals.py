class Solution:

    # based on my understanding of Leetcode/57. Insert Interval.py
    # needed to sort intervals by the 0th index values of each element

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # the actual syntax to do this should be intervals.sort(key = lambda i : i[0])
        intervals = sorted(intervals)
        res = []
        last = intervals[0]

        for i in range(1, len(intervals)):

            if last[1] < intervals[i][0]:
                res.append(last)
                last = intervals[i]
        
            else:
                # note that last = [last[0], max(last[1], intervals[i][1])] also works since we already know the beginning of the "last" interval MUST be smaller (or equal) since it has appeared first in a sorted list
                last = [min(last[0], intervals[i][0]), max(last[1], intervals[i][1])]
        
        res.append(last)
        return res