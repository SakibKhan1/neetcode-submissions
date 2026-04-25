class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        calc = len(nums) / 3 
        res = [] 
        for key, value in counter.items():
            if value > calc:
                res.append(key)

        return res