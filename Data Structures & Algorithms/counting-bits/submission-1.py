class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(n + 1):
            count = 0
            x = i
            while x > 0:
                lastbit = x & 1        # check if last bit is 1
                if lastbit == 1:
                    count += 1
                x = x >> 1                # shift right to check next bit
            res[i] = count             # store the number of 1's for i

        return res
