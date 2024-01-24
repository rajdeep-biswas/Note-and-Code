class Solution:

    # based on my understanding of Leetcode/57. Insert Interval.py
    # needed to sort intervals by the 0th index values of each element

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)
        res = []
        last = intervals[0]

        for i in range(1, len(intervals)):

            if last[1] < intervals[i][0]:
                res.append(last)
                last = intervals[i]
        
            else:
                last = [min(last[0], intervals[i][0]), max(last[1], intervals[i][1])]
        
        res.append(last)
        return res