class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        smallest = min(strs, key = len) 

        res = "" 

        for i in range(len(smallest)):
            for j in strs:
                if j[i] != smallest[i]:
                    return res 
            res += j[i] 

        return res 