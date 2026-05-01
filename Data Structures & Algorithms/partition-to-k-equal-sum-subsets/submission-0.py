class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        length = sum(nums) // k

        sides = [0 for i in range(k)]
        if sum(nums) % k != 0:
            return False
        def dfs(i):
            if i == len(nums):
                return True 

            for side in range(len(sides)):
                if sides[side] + nums[i] <= length:
                    sides[side] += nums[i] 
                    if dfs(i + 1) == True:
                        return True 

                    sides[side] -= nums[i] 

            return False 

        return dfs(0)
              