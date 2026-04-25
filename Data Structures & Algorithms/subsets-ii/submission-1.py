class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # sort so duplicates are adjacent

        def dfs(i, path):
            # base case: reached end of array
            if i == len(nums):
                res.append(path.copy())
                return

            # include nums[i]
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()  # undo inclusion

            # skip duplicates while moving to next index
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # exclude nums[i]
            dfs(i + 1, path)

        dfs(0, [])
        return res
