class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1 

        while left <= right: 
            #found the pivot point 
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break 
            mid = (left + right) // 2
            res = min(nums[mid], res)
            if nums[left] < nums[mid]:
                left = mid + 1 

            elif nums[left] >= nums[mid]:
                right = mid - 1 
        return res 