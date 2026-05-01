class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0 

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                counter += 1 

        return counter