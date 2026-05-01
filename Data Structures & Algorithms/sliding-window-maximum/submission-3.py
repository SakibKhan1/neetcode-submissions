from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        right = 0 
        res = []
        while right < len(nums):
            while queue and nums[right] > queue[-1]:
                queue.pop() 

            queue.append(right)
            if left > queue[0]:
                queue.popleft() 
                
            if (right + 1) >= k: 
                res.append(nums[queue[0]])
                left += 1 



            right += 1
        return res 