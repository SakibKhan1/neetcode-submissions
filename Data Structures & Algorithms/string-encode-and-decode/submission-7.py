class Solution:

    def encode(self, strs: List[str]) -> str:
        #turn it into a string with a separator between each 
        # word and give length of each word into the separator
        # such as "4!" and then after # we count 4 chars to extract 
        res = "" 
        for i in strs:
            length = len(i) 
            res += str(length) + "!" + i 
        return res 
        

    #decode this -> "5!Hello5!World" 
    def decode(self, s: str) -> List[str]:
        i = 0  
        res = [] 
        while i < len(s):
            j = i 
            while s[j] != "!":
                j += 1 
            length = int(s[i: j])
            word = s[j+1: j + length + 1]
            res.append(word)
            i += length + 1 + j
            
            
        return res 