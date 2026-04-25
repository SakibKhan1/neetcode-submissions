class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        word_set = set(dictionary)

        dp = [0] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            # Option 1: skip current character
            dp[i] = 1 + dp[i + 1]

            # Option 2: try all substrings starting at i
            for j in range(i + 1, n + 1):
                if s[i:j] in word_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[0]