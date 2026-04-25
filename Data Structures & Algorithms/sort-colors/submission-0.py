from collections import defaultdict 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)

        for i in range(len(nums)):
            if counter[0] > 0:
                nums[i] = 0 
                counter[0] -= 1
            elif counter[1] > 0:
                nums[i] = 1 
                counter[1] -= 1
            elif counter[2] > 0: 
                nums[i] = 2 
                counter[2] -= 1 

        