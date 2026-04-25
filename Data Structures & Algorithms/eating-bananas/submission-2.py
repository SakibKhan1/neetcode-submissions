class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #the max number it will ever be is the max(inPiles)
        #so it is guaranteed to be a number in the range of 1 to max(piles) 
        #given we know that it's a range between that and it's sorted going up consecutively i want
        #to use binary search to find a value that results in p in piles doing p / middle <= h

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
            elif totalcounter > h: 
                left = middle + 1 
        return res 