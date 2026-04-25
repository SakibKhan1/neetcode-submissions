class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1 
        res = 0 

        while left < right:
            local = 0 
            if heights[left] <= heights[right]:
                local = heights[left] * (right - left) 
                left += 1 
            elif heights[right] < heights[left]:
                local = heights[right] * (right - left)
                right -= 1 

            res = max(res, local) 

        return res 