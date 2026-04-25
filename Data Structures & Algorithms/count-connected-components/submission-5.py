class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        components = 0
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in adj[node]:
                dfs(i)

        for i in range(n):
            if i not in visited:
                dfs(i) 
                components += 1


        return components
