class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        n = len(candidates)
        for i in range(n):
            for j in range(i + 1, n):
                difference = abs(candidates[i] - candidates[j])
                for k in range(i, j):
                    if k == difference:
                        curr.append([candidates[i], candidates[j], candidates[k]])

        return curr 