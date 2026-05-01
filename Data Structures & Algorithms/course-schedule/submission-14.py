from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for crs, prereq in prerequisites:
            adjlist[crs].append(prereq) 
        visited = set() 
        def dfs(crs):
            if adjlist[crs] == []:
                return True 

            if crs in visited:
                return False 

            visited.add(crs) 

            for i in adjlist[crs]:
                if dfs(i) == False:
                    return False 

            visited.remove(crs)
            return True 

        for i in range(numCourses):
            if dfs(i) == True:
                return True
            else:
                return False 