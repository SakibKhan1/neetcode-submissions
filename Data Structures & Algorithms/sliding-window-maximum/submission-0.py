class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] 
        left = 0 
        right = 0 
        while right < len(nums):
            if right < k - 1: 
                right += 1 
                continue 

            windowavg = max(nums[left:right + 1])
            res.append(windowavg) 
            left += 1 
            right += 1 

        return res 

            