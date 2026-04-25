class Solution:

    def encode(self, strs: List[str]) -> str:
        result = "" 
        for i in strs:
            length = len(i) 
            result += str(length) + "#" + i
        return result 
        
    def decode(self, s: str) -> List[str]:
        # s = "3#yes2#no" 
        res = [] 
        i = 0 
        while i < len(s): 
            j = i 
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            res.append(s[j+1: j+1 + length])
            i = j + length + 1
        return res 