class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0 
        for i in range(len(nums) + 1):
            total ^= i
        othertotal = 0 
        for i in nums:
            othertotal ^= i

        return total ^ othertotal 