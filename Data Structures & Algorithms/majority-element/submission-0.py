class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums) 
        res = 0 
        for key, value in counter.items():
            if value > (n // 2):
                res = key  
        
        return res