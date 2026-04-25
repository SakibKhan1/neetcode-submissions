from collections import defaultdict 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapping = {} 
        for i in nums:
            mapping[i] = mapping.get(i, 0) + 1 

        target = len(nums) / 3 
        res = []
        done = False 
        for key, value in mapping.items():
            if value > target:
                done = True 
                res.append(key) 
        if done == False:
            return [] 
        return res 