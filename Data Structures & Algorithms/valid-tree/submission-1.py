from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        randomdict = defaultdict(list)

        for u,v in edges:
            randomdict[u].append(v)
            randomdict[v].append(u) 

        queue = deque([[0,-1]])
        visitset = set([0]) 
        while queue:
            node, prev = queue.popleft()
            for i in randomdict[node]:
                if i == prev:
                    continue 
                elif i in visitset:
                    return False 
                visitset.add(i) 
                queue.append((i, node))  

        return (len(visitset) == n) 