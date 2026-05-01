class Solution:
    def integerBreak(self, n: int) -> int:
        res = 0 
        for i in range(1, n):
            x = n // i 
            res = max(res, x ** i)

        return res 