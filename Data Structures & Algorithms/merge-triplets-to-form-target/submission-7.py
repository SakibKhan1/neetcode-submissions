class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #get rid of the ones that are more than target at any position since they aren't useful
        a1,b1,c1 = target
        good = set() 
        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue 
            for j in range(len(i)): 
                if i[j] == target[j]:
                    good.add(i[j])

        return True if len(good) == 3 else False 