class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        cycle = set() 
        def dfs(crs):
            if crs in cycle:
                return False


            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            output.append(crs)
            return

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output