class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right 

        def helper(cap): 
            ships, currCap = 1, cap 
            for w in weights: 
                if currCap - w < 0:
                    ships += 1 
                    if ships > days:
                        return False 
                    currCap = cap

                currCap -= w 
            return True 

        while left <= right: 
            mid = (left + right) // 2
            if helper(mid) == True:
                res = mid 
                right = mid - 1 

            else:
                left = mid + 1 

        return res 