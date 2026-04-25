class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = [] 
        mapping = defaultdict(list)
        for crs, prereq in prerequisites:
            mapping[crs].append(prereq)
        visiting = set() 
        processed = set() 

        def dfs(crs):
            if crs in visiting: 
                return False 
            if crs in processed:
                return True 

            visiting.add(crs) 

            for i in mapping[crs]:
                if dfs(i) == False: 
                    return False 

            visiting.remove(crs)
            processed.add(crs)
            res.append(crs)
            return True 

        for i in range(numCourses):
            if dfs(i) == False:
                return [] 

        return res 