class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] = minimum number of perfect squares that sum to i
        dp = [float('inf')] * (n + 1)

        dp[0] = 0  # base case

        for i in range(1, n + 1):
            res = float('inf')
            j = 1
            while j * j <= i:
                res = min(res, dp[i - (j * j)] + 1)
                j += 1
            dp[i] = res

        return dp[n]


