class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        #value % 26
        res = [] 
        letter_map = {i: chr(ord('A') + i - 1) for i in range(1, 27)}

        if columnNumber == 1:
            return "A" 
        secondstep = columnNumber // 26
        res.append(letter_map[secondstep])
        firststep = columnNumber % 26
        res.append(letter_map[firststep])


        return "".join(res) 