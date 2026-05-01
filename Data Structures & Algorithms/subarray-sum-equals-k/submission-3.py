class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0 
        for i in range(len(nums)):
            curr = 0 
            for j in range(i, len(nums)):
                curr += nums[j] 
                if curr == k:
                    res += 1 

        return res