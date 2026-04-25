class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        res = x
        bit = 0

        while n:
            if (x & (1 << bit)) == 0:
                if n & 1:
                    res |= (1 << bit)
                n >>= 1
            bit += 1

        return res
