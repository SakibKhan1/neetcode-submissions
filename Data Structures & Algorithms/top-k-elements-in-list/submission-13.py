class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort method 

        freqcounter = [[] for i in range(len(nums) + 1)]
        numdict = {} 
        for num in nums:
            numdict[num] = numdict.get(num,0) + 1 

        for key,val in numdict.items():
            freqcounter[val].append(key) 
        counter = 0
        res = [] 
        for i in range(len(freqcounter) -1, 0, -1):
            for num in freqcounter[i]:
                res.append(num)
                if len(res) == k:
                    return res 
                