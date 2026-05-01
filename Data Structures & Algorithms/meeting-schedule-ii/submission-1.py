"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        result = 1
        if not intervals:
            return 0 
        intervals.sort(key = lambda i: i.start)
        for i in range(1, len(intervals)):
            inter1 = intervals[i-1]
            inter2 = intervals[i]
            if inter2.start < inter1.end:
                result += 1 
        return result  