class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 

        potential = len(nums) 

        #instead of finding a specific value, let's find the 2 pointer/ranges
        while left <= right:
            mid = (left + right) // 2


            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1 

            elif nums[mid] > target: 
                potential = mid 
                right = mid - 1 

        return potential