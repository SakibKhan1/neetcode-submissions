import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBan = max(piles)
        left, right = 1, maxBan

        while left <= right:
            mid = (left + right) // 2
            local = 0
            for i in piles:
                local += math.ceil(i / mid)
            if local > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
