class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        if sum(nums) < target:
            return 0 
        for i in range(len(nums)):
            curr = 0 
            currsteps = 0 
            for j in range(i, len(nums)):
                curr += nums[j]
                currsteps += 1
                if curr >= target:
                    res = min(res, currsteps)

        return res 