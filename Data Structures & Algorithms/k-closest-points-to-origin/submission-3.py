import math
import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = [] 
        
        for x,y in points:
            dist = (x ** 2) + (y ** 2)
            res.append([dist, x, y])
        heapq.heapify(res) 
        i = 0 
        output = [] 
        while i < k: 
            dist, x, y = heapq.heappop(res) 
            output.append([x,y])
            i += 1 

        return output 
