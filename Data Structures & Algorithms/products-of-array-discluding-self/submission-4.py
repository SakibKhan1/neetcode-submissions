class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = nums[i - 1] * res[i - 1]
        res2 = [1] * len(nums) 
        for i in range(len(nums) - 2, -1, -1):
            res2[i] = nums[i + 1] * res2[i + 1]
        res3 = [] 
        for i in range(len(res)):
            res3.append(res[i] * res2[i])
        return res3