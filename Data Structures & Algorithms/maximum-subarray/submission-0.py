class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0 
        result = nums[0]
        
        for i in nums: 
            curr_sum += i 
            if curr_sum < 0: 
                curr_sum = 0  
            result = max(curr_sum, result)
        return result 