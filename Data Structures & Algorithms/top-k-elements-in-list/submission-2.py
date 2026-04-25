import heapq 
from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = [] 
        freqdict = Counter(nums) 
        minheap = [(-freq,num) for num, freq in freqdict.items()]
        heapq.heapify(minheap) 

        for i in range(k):
            kpopped = heapq.heappop(minheap)
            res.append(kpopped[1])

        return res 