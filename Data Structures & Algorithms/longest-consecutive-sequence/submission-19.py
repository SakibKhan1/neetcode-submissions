class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        if not nums:
            return 0 
        
        res = 1 
        for num in nums:
            localres = 1 
            while (num + 1) in setnums:
                localres += 1 
                res = max(res, localres)
                num += 1 
        return res 