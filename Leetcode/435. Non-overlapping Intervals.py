class Solution:

    # watched neetcode video for intuition

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda pair: pair[0])

        last_interval = intervals[0]

        removal_count = 0

        for i in range(1, len(intervals)):

            # in case of an overlap we “remove” the interval that ends later
            if last_interval[1] > intervals[i][0]:

                # by choosing last_interval based on that decision
                if last_interval[1] > intervals[i][1]:
                    last_interval = intervals[i]

                # "else" we keep the last_interval as is, since it "ends sooner"

                removal_count += 1
            
            else:
                last_interval = intervals[i]

        return removal_count