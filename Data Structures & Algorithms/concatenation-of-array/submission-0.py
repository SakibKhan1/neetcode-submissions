class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newarray = [] 

        for i in nums: 
            newarray.append(i)

        return nums + newarray 