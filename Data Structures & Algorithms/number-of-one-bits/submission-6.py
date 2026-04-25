class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0 

        while n:
            last_bit = n % 2 
            if last_bit == 1:
                counter += 1 

            n >>= 1
        return counter 