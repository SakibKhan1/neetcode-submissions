class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        newlist = []  
        for key,value in counter.items():
            newlist.append([value,key])

        heapq.heapify(newlist) 
        while len(newlist) != k:
            heapq.heappop(newlist)

        res = []
        for i in range(len(newlist)):
            res.append(newlist[i][1])
        return res 