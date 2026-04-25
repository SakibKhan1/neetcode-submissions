class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)

        # Smash until ≤ 1 stone remains
        while len(maxheap) > 1:
            a = -heapq.heappop(maxheap)   # heaviest
            b = -heapq.heappop(maxheap)   # 2nd heaviest

            if a != b:
                heapq.heappush(maxheap, -(abs(a - b)))

        return -maxheap[0] if maxheap else 0