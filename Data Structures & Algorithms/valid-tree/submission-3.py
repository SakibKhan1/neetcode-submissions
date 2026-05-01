class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = defaultdict(list) 
        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u) 
        visited = set() 
        
        def dfs(prev, curr):
            if curr in visited:
                return False 
            visited.add(curr)
            for j in adjlist[curr]:
                if j == prev:
                    continue 
                
                if dfs(curr,j) == False:
                    return False 
            return True 

        return dfs(-1,0) 