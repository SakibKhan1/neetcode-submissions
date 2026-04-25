class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallestword = min(strs, key = len)
        res = "" 
        for i in range(len(smallestword)):
            for word in strs:
                if word[i] != smallestword[i]:
                    return res 
            res += smallestword[i]

        return res 