class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = "" 

        smallest = min(len(word1), len(word2))
        pointer1 = 0
        pointer2 = 0 

        while pointer1 < smallest and pointer2 < smallest:
            res += word1[pointer1]
            pointer1 += 1 
            res += word2[pointer2]
            pointer2 += 1 

        if smallest == len(word1):
            res += word2[pointer2: len(word2)]
        elif smallest == len(word2):
            res += word1[pointer1: len(word1)]

        return res 