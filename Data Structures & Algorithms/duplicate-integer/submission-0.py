class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        emptylist = [] 
        for i in nums:
            if i in emptylist:
                return True
            emptylist.append(i)
        return False