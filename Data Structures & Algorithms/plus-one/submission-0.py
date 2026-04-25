class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        b = ''.join(str(num) for num in digits) 
        c = int(b) + 1 
        d = str(c) 
        e = list(d)
        return e