class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() 
        counter = 0 
        marked = [False] * len(intervals) 
        for i in range(1, len(intervals) - 1):
            if intervals[i][0] < intervals[i-1][1] and intervals[i][1] > intervals[i + 1][0]:
                    marked[i] = True 
                    counter += 1 

        return counter 