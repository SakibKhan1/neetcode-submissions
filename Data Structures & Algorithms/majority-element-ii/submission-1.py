from collections import defaultdict 
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = [] 
        counter1 = 0
        counter2 = 0
        cand1 = float('inf')
        cand2 = float('inf')
        for i in range(len(nums)):
            if cand1 == float('inf') or cand2 == float('inf'):
                if cand1 == float('inf'):
                    cand1 = nums[i]
                    counter1 += 1 
                else:
                    cand2 = nums[i]
                    counter2 += 1  

            if nums[i] != cand1 and nums[i] != cand2:
                counter1 -= 1
                counter2 -= 1
                if counter1 == 0:
                    cand1 = float('inf') 
                if counter2 == 0:
                    cand2 = float('inf')
            elif cand1 == nums[i]:
                counter1 += 1 
            elif cand2 == nums[i]:
                counter2 +=1 

        length = len(nums) / 3 
        if counter1 > length:
           res.append(cand1)
        if counter2 > length:
            res.append(cand2)
        return res  