from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = Counter(nums)
        maxHeap = [] 
        for key,value in counter.items():
            maxHeap.append([-value,key])
        heapq.heapify(maxHeap)
        i = 0 
        while i < k:
            res.append(heapq.heappop(maxHeap)[1])
            i += 1 

        return res