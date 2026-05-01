class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1 
        currMin = 1 
        res = 0 
        
        for i in nums: 
            temp = currMax
            currMax = max(i * currMax, i * currMin, i)
            currMin = min(i * currMin, i * temp, i)
            res = max(currMax, res) 

        return res 
        