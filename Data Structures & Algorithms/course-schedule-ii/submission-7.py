from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mapping = defaultdict(list)
        for crs, prereq in prerequisites:
            mapping[crs].append(prereq)

        res = []
        visiting = set()     # courses in current DFS path
        processed = set()    # fully completed courses

        def dfs(crs):
            if crs in visiting:      # cycle detected
                return False
            if crs in processed:     # already done
                return True

            visiting.add(crs)

            for pre in mapping[crs]:
                if dfs(pre) == False:
                    return False

            visiting.remove(crs)
            processed.add(crs)
            res.append(crs)
            return True

        # Must try DFS on ALL courses
        for c in range(numCourses):
            if dfs(c) == False:
                return []

        return res
