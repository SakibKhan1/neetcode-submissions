class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: empty string or starting with '0' → no valid decodings
        if not s or s[0] == '0':
            return 0

        # dp[i] = number of ways to decode up to index i-1
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # empty string has 1 way to decode
        dp[1] = 1  # first char (already checked not '0')

        for i in range(2, len(s) + 1):
            one = int(s[i - 1: i])          # last one digit
            two = int(s[i - 2:i])        # last two digits

            # If the single digit is valid (1–9)
            if 1 <= one <= 9:
                dp[i] += dp[i - 1]

            # If the two digits form a valid code (10–26)
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]
