class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        # 2) DFS helper
        def dfs(curr, target, visited, product):
            # If we reached the target, return the accumulated product
            if curr == target:
                return product

            visited.add(curr)

            for neighbor, weight in graph[curr]:
                if neighbor not in visited:
                    result = dfs(
                        neighbor,
                        target,
                        visited,
                        product * weight
                    )
                    if result != -1:
                        return result

            return -1

        # 3) Process queries
        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1)
            else:
                res.append(dfs(a, b, set(), 1.0))

        return res