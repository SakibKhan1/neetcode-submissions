class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0 
        def backtrack(i, currVal):
            nonlocal res 
            if i == len(nums):
                res += currVal 
                return 

            backtrack(i + 1, currVal ^ nums[i])
            backtrack(i + 1, currVal) 
        backtrack(0, 0) 
        return res 
