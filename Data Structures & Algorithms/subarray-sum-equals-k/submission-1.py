class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = {0: 1} 
        res = 0 
        local = 0 
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(i, 0) + 1 
            local += nums[i] 
            if (local - k) in counter:
                res += 1 

        return res 