class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0 
        for i in range(32):
            last_bit = n & 1
            if last_bit ^ 0 == 1:
                result += 1
            n = n >> 1 
        return result 