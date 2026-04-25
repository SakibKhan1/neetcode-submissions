class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # one way to make sum 0 (choose nothing)

        for t in range(1, target + 1):
            for num in nums:
                if t - num >= 0:
                    dp[t] += dp[t - num]

        return dp[target]
