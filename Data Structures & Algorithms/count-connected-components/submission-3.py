from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapping = defaultdict(list)
        visited = set() 
        counter = 0 
        for u,v in edges:
            mapping[u].append(v)
            mapping[v].append(u)

        for i in range(n):
            if i not in visited:
                counter += 1
                for x in mapping[i]:
                    visited.add(x) 
                continue 
            for j in mapping[i]: 
                visited.add(j) 

        return counter