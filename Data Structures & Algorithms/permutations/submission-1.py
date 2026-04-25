class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        curr = [] 
        used = set() 
        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
            #decision 1: add this number to curr and then add
            # it to used 
            for i in range(len(nums)):
                if nums[i] not in used:
                    curr.append(nums[i])
                    used.add(nums[i])
                    backtrack()
                    curr.pop()
                    used.remove(nums[i])
        backtrack()
        return res

            
            