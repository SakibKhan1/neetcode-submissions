class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        emptydict = {} 
        for i in range(len(nums)):
            difference = target - nums[i] 
            if difference in emptydict:
                return [emptydict[difference], i]
            emptydict[nums[i]] = i 

