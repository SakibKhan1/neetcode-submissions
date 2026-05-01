class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #mod it by len(nums) 

        left, right = 0, k
        counter = k
        n = len(nums) 
        while counter != 0:
            temp1 = nums[left]
            temp2 = nums[right] 
            nums[left], nums[right] = temp2, temp1
            left += 1 
            right += 1 

            if left >= len(nums):
                left = left % n 
            if right >= len(nums):
                right = right % n  

            counter -= 1