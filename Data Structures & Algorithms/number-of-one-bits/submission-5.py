class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        for i in range(32): 
            lastbit = n & 1 
            if lastbit == 1:
                res += 1 

            n >>= 1 

        return res 

