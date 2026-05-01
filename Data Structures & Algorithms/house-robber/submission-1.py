class Solution:
    def rob(self, nums: List[int]) -> int:
        counter1 = 0 
        counter2 = 0
        for i in range(0, len(nums), 2):
            counter1 += nums[i]

        for i in range(1, len(nums), 2):
            counter2 += nums[i]

        return max(counter1, counter2) 
        