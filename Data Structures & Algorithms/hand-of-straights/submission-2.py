from collections import Counter
import heapq 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        freqdict = Counter(hand)

        minheap = [i for i in set(hand)]
        heapq.heapify(minheap)
        while minheap:
            minVal = minheap[0]
            for i in range(minVal, minVal + groupSize):
                if i not in freqdict:
                    return False

                freqdict[i] -= 1 

                if freqdict[i] == 0: 
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap) 
                    del freqdict[i]
        return True 