import heapq
import math 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [] 
        distances = [] 
        for x,y in points: 
            calc = math.sqrt((x - 0) ** 2 + (y - 0) ** 2)
            distances.append((calc, [x,y]))
        heapq.heapify(distances)
        i = 0 
        while i < k:
            coordinate = heapq.heappop(distances)[1]
            res.append(coordinate)
            i += 1 
        return res 