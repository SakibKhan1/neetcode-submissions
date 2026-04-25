import math 
import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        store = [] 
        for x,y in points:
            dist = math.sqrt((x) ** 2 + (y) ** 2)
            store.append([dist,x,y])

        heapq.heapify(store)

        i = 0 
        res = [] 
        while i < k: 
            dist, x, y = heapq.heappop(store) 
            res.append([x,y])
            i += 1 
        
        return res 