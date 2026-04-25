from collections import defaultdict 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for crs, prereq in prerequisites:
            adjList[crs].append(prereq)
        visited = set() 
        def dfs(crs):
            if adjList[crs] == []:
                return True 

            if crs in visited:
                return False 
            visited.add(crs)
            for i in adjList[crs]:
                if dfs(i) == False:
                    return False 

            visited.remove(crs)
            return True  

        for c in range(numCourses):
            if dfs(c) == False:
                return False 
        
        return True 