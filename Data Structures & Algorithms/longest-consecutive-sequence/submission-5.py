class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums) 
        maxlongest = 0 
        for i in sett: 
            if (i - 1) not in sett:
                length = 1 
                while i + length in sett: 
                    length += 1 
                maxlongest = max(maxlongest, length)

        return maxlongest 