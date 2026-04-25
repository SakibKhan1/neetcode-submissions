from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        cycle = set()  # only track the current recursion stack

        def dfs(crs):
            if crs in cycle:  # found a cycle
                return False
            if prereq[crs] == []:  # no prereqs left
                if crs not in output:  # avoid duplicates
                    output.append(crs)
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)

            # mark this course as fully processed by clearing its prereqs
            prereq[crs] = []  
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
