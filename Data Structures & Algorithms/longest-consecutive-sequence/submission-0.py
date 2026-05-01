class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0 
        length = 0 
        for i in nums:
            if (i - 1) not in sett:
                while (i + length) in sett:
                    length += 1 
                longest = max(longest,length)
        return longest 
         