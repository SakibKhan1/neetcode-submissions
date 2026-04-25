class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = [] 
        visited = set() 
        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 

            for num in nums: 
                if num not in visited:
                    curr.append(num)
                    visited.add(num) 
                    dfs()
                    curr.pop()
                    visited.remove(num) 



                else:
                    continue 

        dfs()
        return res 