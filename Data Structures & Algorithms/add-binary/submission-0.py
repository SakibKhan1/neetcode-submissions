class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decA = int(a, 2)
        decB = int(b, 2)
        total = decA + decB

        return str(bin(total)[2:]) 

        