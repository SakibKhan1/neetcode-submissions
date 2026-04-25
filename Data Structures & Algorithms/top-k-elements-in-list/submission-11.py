class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #maxheap version 
        res = []
        counterdict = {} 
        for num in nums:
            counterdict[num] = counterdict.get(num, 0) + 1 

        maxheap = [] 
        for key,value in counterdict.items():
            maxheap.append([-value, key])

        #ok so maxheap now contains list of lists with first element being negative value 
        heapq.heapify(maxheap )
        i = 0 
        while i < k: 
            ans = heapq.heappop(maxheap)[1]
            res.append(ans)
            i += 1 

        return res 