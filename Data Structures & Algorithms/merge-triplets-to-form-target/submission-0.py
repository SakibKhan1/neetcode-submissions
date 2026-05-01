class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0, 0, 0] 
        for i in range(len(triplets)):
            for j in range(3):
                res[j] = max(res[j], triplets[i][j])

        return True if res == target else False 