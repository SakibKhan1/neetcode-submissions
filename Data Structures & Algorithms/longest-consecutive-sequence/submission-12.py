class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setversion = set(nums)
        res = 0 
        for num in nums:
            length = 0 
            if (num - 1) not in setversion: 
                while (num + length) in setversion:
                    length += 1 
            res = max(length, res)

        return res 