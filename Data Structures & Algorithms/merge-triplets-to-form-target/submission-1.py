class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        visited = set() 

        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue 
            for j in range(len(i)):
                if i[j] == target[j]:
                    visited.add(i[j])

        return len(visited) == 3