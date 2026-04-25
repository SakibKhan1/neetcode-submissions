class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        calc = len(nums) / 2 

        counter = Counter(nums)

        for key,value in counter.items():
            if value > calc:
                return key 
                