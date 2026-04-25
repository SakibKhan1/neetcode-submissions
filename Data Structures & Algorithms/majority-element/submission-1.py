class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0] 
        count = 0 
        for i in nums:
            if i != res:
                count -= 1
                if count < 0:
                    res = i  
            elif i == res:
                count += 1

        return res 

