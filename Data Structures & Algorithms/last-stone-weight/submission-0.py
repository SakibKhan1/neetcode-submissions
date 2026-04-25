import heapq 
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1: 
            x,y = heapq.nlargest(2, stones)
            res = abs(x - y)
            stones.remove(x)
            stones.remove(y) 
            stones.append(res) 
        return stones[0] if stones else 0