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
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 
            right += 1 

            if left >= len(nums):
                left = left % n 
            if right >= len(nums):
                right = right % n  

            counter -= 1

