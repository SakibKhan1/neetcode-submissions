class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0 
        currSum = 0  
        mapping = {0: 1}

        for i in range(len(nums)):
            currSum += nums[i] 
            total = currSum - k 

            if total in mapping:
                res += mapping[total]
            
            if currSum in mapping:
                mapping[currSum] += 1 
            else:
                mapping[currSum] = 1

        return res 