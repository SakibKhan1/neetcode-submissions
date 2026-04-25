from collections import deque, defaultdict 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        randomdict = defaultdict(list) 
        for u,v in edges:
            randomdict[u].append(v)
            randomdict[v].append(u) 
        #randomdict now holds adj list of edges 
        counter = 0 
        visited = set() 


        for i in range(n): 
            if i in visited: 
                continue 
            visited.add(i) 
            counter += 1 

            #go through 0's dependencies
            #purpose of this for loop is to make all dependencies of 0 become visited 
            for j in randomdict[i]:
                queue = deque([j]) 
                if j in visited:
                    continue
                visited.add(j) 
                while queue: 
                    node = queue.popleft() 
                    for x in randomdict[node]:
                        if x not in visited:
                            visited.add(x)
                            queue.append(x)
                        
        return counter 