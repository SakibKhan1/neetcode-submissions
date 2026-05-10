class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        res = float('-inf')
        while left < right:
            calc = (right - left) * min(heights[left], heights[right])
            res = max(res, calc) 
            if heights[left] >= heights[right]:
                right -= 1  
            else:
                left += 1 

        return res 