from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        randomdict = defaultdict(list) 
        for u,v in edges:
            randomdict[u].append(v)
            randomdict[v].append(u)

        counter = 0 
        visited = set() 
        for i in range(n):
            if i in visited:
                continue 
            visited.add(i) 
            counter += 1

            for j in randomdict[i]:
                queue = deque([j])
                visited.add(j) 

                while queue:
                    node = queue.popleft() 
                    for x in randomdict[node]:
                        if x not in visited:
                            visited.add(x) 
                            queue.append(x)

        return counter 