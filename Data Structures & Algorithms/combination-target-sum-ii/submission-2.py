class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        curr = []   

        def dfs(i, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or i == len(candidates):
                return

            # decision 1: include current number
            curr.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            curr.pop()  # backtrack

            # decision 2: skip current number (and duplicates)
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return res
