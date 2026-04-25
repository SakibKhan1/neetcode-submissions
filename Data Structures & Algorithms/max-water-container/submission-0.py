#so i will be the i^th bar 
#and height[i] will be the value at that i^th bar 
#we want to get min(height[x], height[y]) * (y - x)
#two pointers solution 
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxcount = 0 
        while left < right: 
            minimum = min(heights[left], heights[right])
            count = minimum * (right - left)
            maxcount = max(count,maxcount)
            if minimum == heights[left]:
                left += 1

            elif minimum == heights[right]:
                right -= 1 
        return maxcount