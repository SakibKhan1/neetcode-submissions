from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #randomdict is adj list for all of edges         
        randomdict = defaultdict(list)
        for a, b in edges:
            randomdict[a].append(b)
            randomdict[b].append(a)

        visited = set()
        counter = 0

        for start in range(n):
            q = deque([start])
            if start in visited:
                continue

            # found a new component
            counter += 1

            visited.add(start)

            while q:
                node = q.popleft()
                for nei in randomdict[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        return counter