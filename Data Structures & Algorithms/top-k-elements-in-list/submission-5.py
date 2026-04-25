from collections import Counter 
import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort method for o(n) time 
        res = [] 
        counter = Counter(nums)
        count = [[] for i in range(len(nums) + 1)]

        for num,freq in counter.items():
            count[freq].append(num) 

        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)

            if len(res) == k:
                return res 
