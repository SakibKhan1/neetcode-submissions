class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0 
        result = nums[0]
        
        for i in nums: 
            if curr_sum < 0: 
                curr_sum = 0
            curr_sum += i   
            result = max(curr_sum, result)
        return result 