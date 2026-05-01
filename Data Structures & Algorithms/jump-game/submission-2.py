class Solution:
    def canJump(self, nums: List[int]) -> bool:
        flag = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] == flag:
                flag = i 
        return True if flag == 0 else False 