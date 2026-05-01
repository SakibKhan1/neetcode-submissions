class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setversion = set(nums)
        length = 0
        for num in nums:
            if (num - 1) not in setversion: 
                while (num + length) in setversion:
                    length += 1 
                

        return length 