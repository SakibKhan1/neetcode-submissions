class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()
        output = [] 

        #first for loop just puts newInterval in right spot
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                output.append(newInterval)
            output.append(intervals[i])
        if output:
            output2 = [output[0]]
        else:
            return 
        #second for loop just merges them if needed 
        for i in range(1, len(output)):
            if output[i][0] <= output2[-1][1]:
                output2[-1][1] = max(output2[-1][1], output[i][1])
            else:
                output2.append(output[i])

        return output2