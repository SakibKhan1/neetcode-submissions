class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        for i in range(len(nums)):
            local = 0

            for j in range(i, len(nums)):
                local += nums[j] 
                if local == k:
                    res += 1
                
        return res 