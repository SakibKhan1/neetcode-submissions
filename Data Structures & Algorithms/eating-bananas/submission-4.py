import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #the output will always be a number between 1 and max(piles)
        #ceil(piles(i) / num) should total equal/less than h 
        left, right = 1, max(piles)
        res = right 
        while left <= right:
            middle = (left + right) // 2 
            totalcounter = 0 

            for p in piles:    
                totalcounter += math.ceil(p / middle)
            
            if totalcounter <= h: 
                res = middle 
                right = middle - 1 

            else: 
                left = middle + 1 

            
        return res 