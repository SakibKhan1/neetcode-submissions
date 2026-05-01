import math
import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [] 
        
        for x,y in points:
            dist = math.sqrt((x - 0) ** 2 + ((y - 0) ** 2))
            res.append([dist, x, y])

        i = 0 
        output = [] 
        while i < k: 
            dist, x, y = heapq.heappop(res) 
            output.append([x,y])
            i += 1 

        return output 
