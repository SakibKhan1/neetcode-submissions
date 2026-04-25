class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        visited = set()  
        if len(nums) == 1:
            return False 
        for right in range(k + 1):
            if nums[right] in visited:
                return True 
            visited.add(nums[right])

        for right in range(k + 1, len(nums)):
            visited.remove(nums[left])
            left += 1 
            if nums[right] in visited:
                return True 
            visited.add(nums[right])

        return False 