class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        boolval = False 
        for i in wordDict:
            if i in s:
                boolval = True 

        return boolval 