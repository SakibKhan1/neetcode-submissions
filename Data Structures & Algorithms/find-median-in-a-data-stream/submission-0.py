import math

class MedianFinder:

    def __init__(self):
        self.container = []

    def addNum(self, num: int) -> None:
        self.container.append(num)

    def findMedian(self) -> float:
        self.container.sort()
        n = len(self.container)

        if n % 2 == 1:
            mid = n // 2
            return self.container[mid]

        else:
            mid1 = n // 2 - 1
            mid2 = n // 2
            return (self.container[mid1] + self.container[mid2]) / 2
