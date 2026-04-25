class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        length = len(heights)
        maxArea = 0 
        for i in range(length):
            for j in range(i, length):
                sectionMin = float("inf")
                for k in range(i, j + 1):
                    sectionMin = min(sectionMin, heights[k])
                maxArea = max(maxArea, sectionMin * (j - i + 1))

        return maxArea 