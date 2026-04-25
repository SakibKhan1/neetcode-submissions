class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []


        for i in range(n + 1):
            local = 0 
            for j in range(32):  
                lastbit = i & 1
                if lastbit == 1:
                    local += 1 
                i >>= 1 
            output.append(local) 

        return output 