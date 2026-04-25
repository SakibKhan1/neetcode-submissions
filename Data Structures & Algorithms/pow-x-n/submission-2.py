class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            #x is the base, n is the exponent 

            if n == 0:
                return 1 
            if x == 0:
                return 0 

            result = helper(x * x, n // 2) 
            if n % 2 == 0:
                return result 
            else:
                return x * result 

        answer = helper(x,abs(n))
        if n >= 0:
            return answer
        else:
            return (1 / answer) 