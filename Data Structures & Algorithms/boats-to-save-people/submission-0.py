class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        nums = sorted(people)
        left, right = 0, len(people) - 1 
        res = 0 
        while left <= right: 
            if right == left:
                res += 1 
                left += 1 
                right -= 1 
            elif nums[left] + nums[right] > limit:
                res += 1 
                right -= 1

            elif nums[left] + nums[right] <= limit:
                res += 1 
                left += 1 
                right -= 1 

        return res 