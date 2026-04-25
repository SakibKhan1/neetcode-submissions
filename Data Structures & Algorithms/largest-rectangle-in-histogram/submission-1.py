class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        
        # Step 1: next smaller to left
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        # Step 2: next smaller to right
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        # Step 3: compute max area
        maxArea = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            maxArea = max(maxArea, heights[i] * width)
        
        return maxArea
