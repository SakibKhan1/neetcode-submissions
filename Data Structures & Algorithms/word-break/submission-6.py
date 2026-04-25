class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)

        dp = [False] * (len(s) + 1)

        #dp[0] returns 1 since empty string can be segmented with wordDict 
        dp[0] = True 
        
        for i in range(1, len(s) + 1):
            for j in range(i): 
                if dp[j] == True and s[j:i] in wordset:
                    dp[i] = True 
        return dp[len(s)]