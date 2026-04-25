from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mapping = defaultdict(list)

        for u,v in trust:
            mapping[v].append(u)

        #{1: [] 2: [] 3: [1,4,2]}
        found = False 
        for key,value in mapping.items():
            if len(value) == len(trust):
                found = True 
                return key 
            
        if found == False:
            return -1 