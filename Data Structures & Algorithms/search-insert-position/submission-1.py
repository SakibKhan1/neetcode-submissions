class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        res = len(nums)

        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target: 
                return mid 

            elif nums[mid] < target:
                left = mid + 1 

            elif nums[mid] > target:
                res = mid 
                right = mid - 1 

        return res 