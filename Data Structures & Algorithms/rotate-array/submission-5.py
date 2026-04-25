class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1 
        k = k % len(nums) 

        while left < right:
            nums[left], nums[right] = nums[right], nums[left] 
            left += 1 
            right -= 1 

        l1, r1 = 0, k - 1 
        while l1 < r1:
            nums[l1], nums[r1] = nums[r1], nums[l1]
            l1 += 1 
            r1 -= 1

        l2, r2 = k, len(nums) - 1 
        while l2 < r2:
            nums[l2], nums[r2] = nums[r2], nums[l2]
            l2 += 1 
            r2 -= 1