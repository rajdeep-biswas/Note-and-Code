class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # based on my understanding (and dry running) of neetcode's code

        res = []
        
        for i in range(len(intervals)):

            # if the new interval fits in _before_ the current index interval, just putting the remaining list after it and return
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            
            # else, if the current index interval fits cleanly _before_ the new interval, put the interval safely into results and move on with newInterval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # the "else" means the current index and new intervals are overlapping (since neither does the latter fit before or after). when that is the case, update the newInterval to be covering the start and end of both the intervals (if that makes sense)
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])]
        
        # remember we still haven't inserted the new (updated) interval if the code never hit the line 11 'if', so we need to do it here
        res.append(newInterval)

        return res