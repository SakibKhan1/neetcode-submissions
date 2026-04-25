class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        randomdict = defaultdict(list)
        visitset = set() 

        for i,j in edges:
            randomdict[i].append(j)
            randomdict[j].append(i) 

        queue = deque([[0, -1]])
        visitset.add(0) 

        while queue:
            node, prev = queue.popleft() 
            for i in randomdict[node]:
                if i == prev:
                    continue 
                if i in visitset:
                    return False
                queue.append((i, node)) 
                visitset.add(i) 

        return len(visitset) == n 

