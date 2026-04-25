class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set() 
        while n not in sett: 
            sett.add(n) 
            n = self.calculation(n) 
            if n == 1: 
                return True 
        return False 
        
    def calculation(self, n: int): 
        result = 0 
        while n != 0: 
            last_digit = n % 10 
            last_digit = last_digit ** 2 
            result += last_digit 
            n = n // 10 
        return result 
