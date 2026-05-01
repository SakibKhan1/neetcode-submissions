class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #make a hashmap where it is coursenum : list of prereqs 
        hashmap = {i: [] for i in range(numCourses)}
        visited = set() 

        for crs, prereq in prerequisites:
            hashmap[crs].append(prereq)

        def dfs(crs):
            if crs in visited:
                return False 

            if hashmap[crs] == []: 
                return True 

            visited.add(crs)

            for prereq in hashmap[crs]:
                if not dfs(prereq):
                    return False 

            #at this point, we know it is cycle free, so we can safely remove from visitset
            visited.remove(crs)
            hashmap[crs] = [] 
            return True 


        for c in range(numCourses):
            if not dfs(c):
                return False 
            return True 
            
