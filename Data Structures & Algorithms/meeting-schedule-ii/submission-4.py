import heapq 
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minheap = [] 
        intervals.sort(key=lambda x:x.start)
        heapq.heapify(minheap)
        for i in intervals:
            heapq.heappush(minheap, i.end)

        for i in intervals:
            if minheap and i.start >= minheap[0]:
                heapq.heappop(minheap) 
        

        return len(minheap)