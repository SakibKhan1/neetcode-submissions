class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curr = []
        used = [False] * len(nums)

        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                curr.append(nums[i])
                used[i] = True
                dfs()
                curr.pop()
                used[i] = False

        dfs()
        return res
 