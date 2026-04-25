class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        output = []
        inserted = False 

        for i in range(len(intervals)):
            if not inserted and newInterval[0] < intervals[i][0]:
                inserted = True
                output.append(newInterval)

            output.append(intervals[i])
        if not inserted:
            output.append(newInterval)

        res = [output[0]]

        for i in range(1, len(output)):
            if output[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], output[i][1])
            else:
                res.append(output[i]) 
        return res 