class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        curr = 0 
        for i in bills:
            if i == 5:
                curr += 5 
            elif i == 10: 
                if curr < 5:
                    return False 
                curr += 5  

            elif i == 20:
                if curr < 15:
                    return False 
                curr += 15

        return True 
            