class Solution:
    def findRedundantConnection(self, edges):
        adj = [[] for _ in range(len(edges) + 1)]

        def dfs(curr, target, visited):
            if curr == target:
                return True
            visited.add(curr)

            for nei in adj[curr]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True

            return False

        for u, v in edges:
            # Case 1: before adding, check if u and v are already connected
            visited = set()
            if adj[u] and adj[v] and dfs(u, v, visited):
                return [u, v]

            # Case 2: safe to add the edge
            adj[u].append(v)
            adj[v].append(u)

        return []
