class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0 

        while n:
            last_bit = n % 2 
            counter += last_bit ^ 0 

            n >>= 1
        return counter 