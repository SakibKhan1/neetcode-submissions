class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0 
        for i in nums:
            localcounter = 1
            if (i - 1) not in numsSet:
                j = i 
                while (j + 1) in numsSet:
                    localcounter += 1 
                    j += 1 
            res = max(localcounter, res)

        return res 