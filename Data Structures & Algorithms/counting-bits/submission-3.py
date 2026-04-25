class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [] 
        
        for i in range(n + 1):
            counter = 0 
            while i:
                lastbit = i % 2 
                if lastbit == 1: 
                    counter += 1
                i >>= 1  
            res.append(counter)
        return res 