from collections import Counter 
import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = [] 
        max_heap = [[-freq,num] for num, freq in counter.items()]
        heapq.heapify(max_heap) 

     
        i = 0 
        while i < k: 
            res.append(heapq.heappop(max_heap)[1])
            i += 1 

        return res 