class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        localres = 1
        res = 1
        for num in nums:
            if num in setnums and num - 1 not in setnums:
                temp = num 
                while (temp + 1) in setnums:
                    localres += 1 
                    res = max(res, localres) 
                    temp += 1 
        return res 