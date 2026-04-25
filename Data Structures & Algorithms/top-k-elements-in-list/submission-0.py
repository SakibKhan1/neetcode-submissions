from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums)+1)]
        freqmap = defaultdict(list) 
        for i in nums:
            freqmap[i] = freqmap.get(i, 0) + 1 
        for key,value in freqmap.items():
            count[value].append(key) 
        res = [] 
        for i in range(len(count) - 1, 0, -1):
            for j in count[i]:
                res.append(j)
                if len(res) == k:
                    return res 
                    