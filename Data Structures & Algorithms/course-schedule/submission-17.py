from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set() 
        mapping = defaultdict(list)
        for crs, prereq in prerequisites:
            mapping[crs].append(prereq)
        
        def dfs(crs, visited):
            if mapping[crs] == []:
                return True 
            if crs in visited:
                return False 
            visited.add(crs)
            for value in mapping[crs]:
                if dfs(value, visited) == False:
                    return False 

            return True 

        for i in range(numCourses):
            if dfs(i, visited) == False:
                return False 

        return True  
