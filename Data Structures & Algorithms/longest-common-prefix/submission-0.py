class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        small = min(strs, key=len)
        res = "" #first iteration: "b" 

        for i in range(len(small)):
            local = small[i]
            for j in strs:
                if j[i] != local:
                    return res 
            res += j[i] 

        return res 


