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

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # sort intervals based on the start time
        intervals.sort(key = lambda x: x.start)

        # simply check for conflicts / overlaps if the end time of nth meeting is after the start time of n+1th meeting
        for i in range(len(intervals) - 1):
            if intervals[i + 1].start < intervals[i].end:
                return False
        return True