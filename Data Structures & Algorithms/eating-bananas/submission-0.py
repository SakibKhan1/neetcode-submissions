from math import ceil 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = ceil(sum(piles)/h), max(piles)
        res = r
        while l <= r:
            k = l + (r - l) // 2
            hrs = 0
            for pile in piles:
                hrs += ceil(pile / k)
                
            if hrs > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        
        return res