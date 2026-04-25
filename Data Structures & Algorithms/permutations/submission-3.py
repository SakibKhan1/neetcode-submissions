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
                    #decision 1: add current number and add it
                    # to used and then recurse forward 
                    curr.append(nums[i])
                    used.add(nums[i])
                    backtrack()

                    #decision 2: pop it and remove it from used
                    #to try other options
                    curr.pop()
                    used.remove(nums[i])
                else:
                    continue
        backtrack()
        return res

            
            