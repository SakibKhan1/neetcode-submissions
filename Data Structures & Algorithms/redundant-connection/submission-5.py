class Solution:
    def findRedundantConnection(self, edges):
        adjlist = [[] for i in range(len(edges) + 1)]

        def dfs(u,v,visited):
            #we are checking if u can connect to v 
            # and so that means that if u is ever same as v through 
            # adjlist that guarantees u and v were connected 

            if u == v: 
                return True

            visited.add(u)

            for neigh in adjlist[u]:
                if neigh not in visited:
                    if dfs(neigh, v, visited) == True:
                        return True 
            return False 

        for u,v in edges:
            visited = set() 
            if dfs(u,v,visited) == True:
                return [u,v]

            adjlist[u].append(v)
            adjlist[v].append(u) 

        return [] 