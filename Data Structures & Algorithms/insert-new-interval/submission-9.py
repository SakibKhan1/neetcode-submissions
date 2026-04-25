class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()           # ensure sorted by start
        output = []
        inserted = False

        # ---- PASS 1: Insert newInterval into correct position ----
        for interval in intervals:
            # Insert once, right before the first interval that starts after newInterval
            if not inserted and interval[0] > newInterval[0]:
                output.append(newInterval)
                inserted = True
            output.append(interval)

        # If newInterval belongs at the end
        if not inserted:
            output.append(newInterval)

        # ---- PASS 2: Merge overlapping intervals ----
        merged = [output[0]]

        for i in range(1, len(output)):
            if output[i][0] <= merged[-1][1]:
                # overlap → extend the current interval
                merged[-1][1] = max(merged[-1][1], output[i][1])
            else:
                merged.append(output[i])

        return merged
