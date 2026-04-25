class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        # dp[i][0] = max profit on day i when we do NOT hold stock
        # dp[i][1] = max profit on day i when we DO hold stock
        dp = [[0, 0] for _ in range(n)]

        dp[0][0] = 0           # no stock, no profit
        dp[0][1] = -prices[0]  # bought stock on day 0

        for i in range(1, n):
            # When not holding: either we did nothing today, or we sold today
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])

            # When holding: either we did nothing today, or we bought today (after cooldown)
            dp[i][1] = max(dp[i-1][1], (dp[i-2][0] if i >= 2 else 0) - prices[i])

        return dp[-1][0]