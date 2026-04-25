class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = [] 


        nums.sort() 
        def backtrack(i):
            if i == len(nums):
                res.append(curr.copy())
                return 

            #first decision is to include it and move to next index

            curr.append(nums[i])
            backtrack(i + 1) 

            curr.pop() 

            #second decision is to skips this number and move to next index
            #but also skip duplicates too  
            while (i + 1 < len(nums) and nums[i] == nums[i + 1]):
                i += 1 
            backtrack(i + 1)

        backtrack(0)
        return res 