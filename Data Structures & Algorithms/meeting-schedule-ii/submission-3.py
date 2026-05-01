"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0 
        counter = 0 
        intervals.sort(key=lambda x:x.start) 
        maxEnd = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start >= maxEnd:
                continue 
            elif intervals[i].start > intervals[i-1].end: 
                counter += 1 
            maxEnd = max(maxEnd, intervals[i].end)

        return counter + 1