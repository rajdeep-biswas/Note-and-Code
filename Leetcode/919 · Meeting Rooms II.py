from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    """
    Neetcode did a hacky solution, so I did not end up learning heaps.
    This was the original source https://walkccc.me/LeetCode/problems/0253/#__tabbed_1_3
    This girl's explanation also helped https://www.youtube.com/watch?v=h_Ej3FFfnek
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here

        intervals.sort(key = lambda pair: pair.start)

        end_times = []

        # we know when the first meeting is ending
        heapq.heappush(end_times, intervals[0].end)

        for interval in intervals[1:]:

            # end_times[0] will always be the meeting that is ending the soonest
            if interval.start >= end_times[0]:
                # if current meeting is starting after (or right at) the soonest ending meeting, 
                # we can remove the soonest meeting from heap, since "it's over"
                heapq.heappop(end_times)
            # since we have started another meeting, we need to keep track of its end time by pushing into heap
            heapq.heappush(end_times, interval.end)

        # by the end, end_times (heap) will contain the meeting ending times after which no meetings started
        return len(end_times)