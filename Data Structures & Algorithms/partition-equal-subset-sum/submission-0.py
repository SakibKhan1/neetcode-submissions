class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0: 
            return True 
        else:
            return False 