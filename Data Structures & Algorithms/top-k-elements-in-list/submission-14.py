class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        visited = set(nums) 
        heapq.heapify(nums) 
        while len(visited) > k: 
            m = heapq.heappop(nums)
            visited.remove(m)

        return list(visited) 