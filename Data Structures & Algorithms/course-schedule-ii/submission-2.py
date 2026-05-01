from collections import defaultdict 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        indegree = [0] * numCourses
        adj = defaultdict(list)  # prereq -> list of courses unlocked by it

        # FIX: edge is b -> a (not a -> b)
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1

        queue = deque(i for i in range(numCourses) if indegree[i] == 0)

        while queue:
            u = queue.popleft()
            res.append(u)
            for v in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        # If there was a cycle, we couldn't schedule all courses
        return res 