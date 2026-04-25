from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mapping = defaultdict(list)
        visitset = set() 
        queue = deque([[0, -1]])

        for u, v in edges:
            mapping[u].append(v)
            mapping[v].append(u) 

        while queue:
            node, prev = queue.popleft() 
            for i in mapping[node]:
                if i == prev:
                    continue 
                elif i not in visitset:
                    visitset.add(i)
                    queue.append((i, node))
                elif i in visitset:
                    return False 
        return ((len(visitset) + 1) == n)