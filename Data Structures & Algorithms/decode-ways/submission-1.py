class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0 or not s:
            return 0 
        dp = [0] * (len(s) + 1) 

        dp[0] = 1 
        dp[1] = 1  

        for i in range(2, len(s) + 1):
            prevOne = int(s[i - 1: i])
            prevTwo = int(s[i - 2: i])
            if 1 <= prevOne <= 9:
                dp[i] += dp[i - 1]
            if 10 <= prevTwo <= 26:
                dp[i] += dp[i - 2] 


        return dp[len(s)]