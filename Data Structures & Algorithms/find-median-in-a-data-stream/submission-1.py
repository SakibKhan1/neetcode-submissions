import heapq

class MedianFinder:

    def __init__(self):
        # max-heap for the *smaller* half of numbers
        # store negatives so Python's min-heap behaves like a max-heap
        self.small = []  

        # min-heap for the *larger* half of numbers
        self.large = []  

    def addNum(self, num: int) -> None:
        # Step 1: always push to max-heap first (as negative)
        heapq.heappush(self.small, -num)

        # Step 2: ensure every num in small <= every num in large
        # move the largest from small to large if needed
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: rebalance sizes so len(small) >= len(large)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # Case 1: odd total → top of the bigger heap
        if len(self.small) > len(self.large):
            return -self.small[0]
        # Case 2: even total → average of both tops
        return (-self.small[0] + self.large[0]) / 2

