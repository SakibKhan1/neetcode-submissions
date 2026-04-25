class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] 
        curr = [] 
        candidates.sort()
        def backtrack(i, total): 
            if total == target:
                res.append(curr.copy())
                return
            if total > target:
                return 
            if i == len(candidates):
                return 
            
            #decision 1: include current number and go to next index
            # to try another number to add to total 
            curr.append(candidates[i])
            backtrack(i + 1, total + candidates[i])

            curr.pop()
            #decision 2: exclude current number to try to use another one
            # at the right while skipping dupes since decision 1
            # already handled all unique indices
            while(i + 1 < len(candidates) and candidates[i] == candidates[i+1]):
                i += 1 
            backtrack(i + 1, total) 
        backtrack(0,0)
        return res 