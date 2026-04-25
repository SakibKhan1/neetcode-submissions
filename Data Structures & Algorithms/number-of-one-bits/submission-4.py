class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0 

        for i in range(32):
            lastbit = n & 1
            if lastbit == 1:
                counter += 1 
            n = n >> 1 

        return counter 