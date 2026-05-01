class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = a & 1
            b_bit = b & 1

            sum_bits = a_bit + b_bit + carry
            cur_bit = sum_bits % 2
            carry = sum_bits // 2

            if cur_bit:
                res += (1 << i) 

            a >>= 1
            b >>= 1



        return res
