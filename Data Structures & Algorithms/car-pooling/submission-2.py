class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []

        # create pickup and dropoff events
        for p, start, end in trips:
            events.append((start, p))    # pickup
            events.append((end, -p))     # dropoff

        # sort by location
        events.sort()

        curr = 0
        for _, change in events:
            curr += change
            if curr > capacity:
                return False

        return True
