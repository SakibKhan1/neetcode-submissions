class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        inputset = set(nums)
        if not nums:
            return 0 
        counter = 1 
        for i in inputset:
            if (i - 1) not in inputset: 
                length = 1 
                while i + length in inputset:
                    length += 1 
                counter = max(length, counter)
            
        return counter 