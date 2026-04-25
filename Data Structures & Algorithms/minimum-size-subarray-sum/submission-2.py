class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left, right = 0, 0 
        currSum = 0 
        while right < len(nums):
            currSum += nums[right] 
            while currSum >= target:
                res = min(res, right - left + 1)
                currSum -= nums[left]  
                left += 1 

            right += 1 

        if res == float('inf'):
            return 0 
        else:
            return res 