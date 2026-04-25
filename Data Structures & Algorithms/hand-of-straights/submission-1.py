class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        minheap = [] 
        for key,value in counter.items():
            minheap.append(key) 

        if len(hand) % groupSize:
            return False  
        heapq.heapify(minheap) 
        while minheap: 
            start = minheap[0]

            for i in range(start, start + groupSize): 
                if i not in minheap:
                    return False 
                counter[i] -= 1 
                if counter[i] == 0: 
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)

        return True 