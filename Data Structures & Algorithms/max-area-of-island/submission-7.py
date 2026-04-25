from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #we want the bfs to return an int giving the area from a 1 
        #max(res, bfs(row,col))
        res = 0 
        rows, cols = len(grid), len(grid[0])
        
        def bfs(row, col): 
            counter = 1 
            queue = deque() 
            queue.append((row,col))  
            grid[row][col] = 0
            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            while queue: 
                row, col = queue.popleft() 
                for dr,dc in directions: 
                    nr = dr + row
                    nc = dc + col 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: 
                        queue.append((nr,nc))
                        grid[nr][nc] = 0 
                        counter += 1 
            return counter 

        for row in range(rows):
            for col in range(cols): 
                if grid[row][col] == 1: 
                    res = max(res, bfs(row, col)) 
                    

        return res 