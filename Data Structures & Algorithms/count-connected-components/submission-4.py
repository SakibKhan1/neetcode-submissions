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
            if i in visited:
                continue 
            counter += 1 
            visited.add(i) 

            for j in mapping[i]:
                queue = deque([j])
                visited.add(j) 
                while queue:
                    node = queue.popleft() 
                    for x in mapping[node]:
                        if x not in visited:
                            visited.add(x) 
                            queue.append(x) 

        return counter 