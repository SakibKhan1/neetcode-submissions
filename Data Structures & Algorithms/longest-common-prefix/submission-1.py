class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallestWord = len(min(strs, key = len))
        res = ""
        for i in range(smallestWord):
            for j in range(smallestWord):
                if strs[i] != strs[j]:
                    return res 
                res += strs[i] 

        return res 