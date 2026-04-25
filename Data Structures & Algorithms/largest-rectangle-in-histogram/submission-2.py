class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] 
        left = [-1] * len(heights) 
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() 
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1

            stack.append(i)

        right = [len(heights)] * len(heights) 
        stack = [] 
        for i in range(len(heights) -1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop() 
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = len(heights)
            stack.append(i)

        for i in range(len(heights)):
            width = right[i] - left[i] - 1 
            maxArea = max(maxArea, width * heights[i])

        return maxArea 