class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        local = 0
        total = 0 

        for i in nums:
            local = local ^ i 

        for i in range(len(nums) + 1):
            total = total ^ i 

        return local ^ total 