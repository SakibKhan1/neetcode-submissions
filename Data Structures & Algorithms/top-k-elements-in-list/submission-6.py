from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        answer = [] 
        res = [[] for i in range(len(nums) + 1)]

        for num, freq in counter.items():
            res[freq].append(num) 

        for i in range(len(res) - 1, 0, -1):
            for j in res[i]:
                answer.append(j) 
                if len(answer) == k:
                    return answer 
