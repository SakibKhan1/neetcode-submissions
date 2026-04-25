class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            n = len(word) 
            res += str(n) + "#" + word
        return res 

    def decode(self, s: str) -> List[str]:
        res = [] 
        i = 0 
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 
            number = int(s[i:j])
            word = s[j + 1: j + number + 1]
            res.append(word)
            i = j + number + 1 

        return res
