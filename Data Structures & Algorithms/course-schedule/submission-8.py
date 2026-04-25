class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {i: [] for i in range(numCourses)}
        visited = set() 

        for crs, prereq in prerequisites:
            hashmap[crs].append(prereq)

        def dfs(crs):
            if hashmap[crs] == []:
                return True 
            if crs in visited:
                return False 
            
            visited.add(crs) 

            for prereq in hashmap[crs]:
                if not dfs(prereq):
                    return False
            
            visited.remove(crs) 
            hashmap[crs] = []  # ✅ Memoize as safe
            return True 

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True 
