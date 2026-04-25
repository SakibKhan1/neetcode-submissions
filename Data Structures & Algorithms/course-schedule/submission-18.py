from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set() 
        mapping = defaultdict(list)
        for crs, prereq in prerequisites:
            mapping[crs].append(prereq)
        
        def dfs(crs):
            if mapping[crs] == []:
                return True 
            if crs in visited:
                return False 
            visited.add(crs)
            for value in mapping[crs]:
                if dfs(value) == False:
                    return False 
            visited.remove(crs)

            return True 

        for i in range(numCourses):
            if dfs(i) == False:
                return False 

        return True  
