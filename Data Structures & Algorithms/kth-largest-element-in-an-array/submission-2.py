class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-num for num in nums]
        heapq.heapify(maxheap)
        res = [] 
        i = 0 
        while i <k: 
            res.append(-heapq.heappop(maxheap))
            i += 1 
        return res[-1]