class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0 

        while True:
            slow = nums[slow]
            fast = nums[nums[slow]]
            if slow == fast:
                break 

        slow2 = 0 
        while True: 
            slow2 = nums[slow2]
            if slow2 == slow:
                return slow2