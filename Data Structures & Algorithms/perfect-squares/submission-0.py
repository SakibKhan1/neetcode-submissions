class Solution:
    def numSquares(self, n: int) -> int:
        def helper(num):
            if num == 1:
                return True 
            for i in range(1, num): 
                if i ** 2 == num:
                    return True 
            return False  
        counter = 0 
        ref = n 
        for i in range(n, -1, -1):
            if helper(i) == True:
                while ref - i >= 0:
                    counter += 1 
                    ref -= i 
                 
        return counter 