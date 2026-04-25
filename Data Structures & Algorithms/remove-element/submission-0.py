class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #how to approach removing elements:
        # we keep a count of where we can switch value with and increment it by 1 after every switch

        count = 0 

        for i in range(len(nums)):
            if nums[i] != val:
                nums[count] = nums[i] 
                count += 1 


        return count 
        