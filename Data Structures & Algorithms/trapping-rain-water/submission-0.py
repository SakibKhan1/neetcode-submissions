class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0 
        left, right = 0, len(height) - 1 
        maxleft = height[left]
        maxright = height[right] 
        if not height:
            return 0 
        while left < right: 
            if maxleft <= maxright:
                left += 1
                maxleft = max(maxleft, height[left])
                count += maxleft - height[left]

            elif maxleft > maxright:  
                right -= 1 
                maxright = max(maxright, height[right])
                count += maxright - height[right] 
        return count 
