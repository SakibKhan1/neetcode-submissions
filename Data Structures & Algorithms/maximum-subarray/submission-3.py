class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(len(nums)):
            total = 0 
            for j in range(i + 1, len(nums)):
                total += nums[j]
                res = max(total, res)

        return res 