import heapq 
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        cooldown = None 
        maxheap = [] 
        res = [] 
        maxFreq = max(counter.values())

        if maxFreq > (len(s) + 1) // 2:
            return ""
        #maxheap has [[-2, "y"], [-1, "a"], [-1, "x"]]
        for key, value in counter.items():
            heapq.heappush(maxheap, [-value, key])
        while maxheap:
            s = heapq.heappop(maxheap)
            res.append(s[1])
            if cooldown: 
                heapq.heappush(maxheap, cooldown)
                cooldown = None 
            s[0] += 1 
            if s[0] < 0: 
                cooldown = s 


        return "".join(res) 