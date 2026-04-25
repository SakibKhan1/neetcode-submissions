class Solution:
    def findRedundantConnection(self, edges):
        adj = [[] for _ in range(len(edges) + 1)]

        def dfs(u, v, visited):
            if u == v:
                return True
            visited.add(u)

            for nei in adj[u]:
                if nei not in visited:
                    if dfs(nei, v, visited):
                        return True


            return False

        for u, v in edges:
            # Case 1: before adding, check if u and v are already connected
            visited = set()
            if dfs(u, v, visited):
                return [u, v]

            # Case 2: safe to add the edge
            adj[u].append(v)
            adj[v].append(u)

        return []
