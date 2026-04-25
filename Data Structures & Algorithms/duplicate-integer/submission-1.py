class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emptyset = set() 
        for i in nums:
            if i in emptyset:
                return True
            emptyset.add(i)
        return False