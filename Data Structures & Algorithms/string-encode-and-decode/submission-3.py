class Solution:

    def encode(self, strs: List[str]) -> str:
        res = "" 
        for word in strs: 
            n = len(word)
            res += str(n) + "#" + word 
        return res 

    def decode(self, s: str) -> List[str]:
        i = 0 
        j = 0 
        res = [] 
        while i < len(s): 
            while s[j] != "#": 
                j += 1 
            number = int(s[i:j])
            res.append(s[j + 1: j + 1 + number])
            j = j + number + 1 
            i = j 
        return res 