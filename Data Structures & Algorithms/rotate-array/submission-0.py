class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, k 

        while right < len(nums):
            temp1 = nums[left] 
            temp2 = nums[right]
            nums[left], nums[right] = temp2, temp1 
            left += 1  
            right += 1 


        