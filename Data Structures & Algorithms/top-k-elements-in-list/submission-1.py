import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqdict = {}
        res = [] 

        for i in nums:
            freqdict[i] = freqdict.get(i,0) + 1 

        heap = [[-freq,num] for num,freq in freqdict.items()]
        heapq.heapify(heap)
        i = 0 
        while i < k:
            res.append(heapq.heappop(heap)[1])  
            i += 1 

        return res 
