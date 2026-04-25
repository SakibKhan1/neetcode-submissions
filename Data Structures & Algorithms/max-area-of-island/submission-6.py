from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxarea = 0 
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def bfs(row, col):
            queue = deque()
            queue.append((row, col)) 
            localcounter = 1 
            grid[row][col] = 0 

            while queue: 
                row, col = queue.popleft() 
                for dr, dc in directions:
                    nr = dr + row 
                    nc = dc + col 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: 
                        queue.append((nr,nc))
                        grid[nr][nc] = 0 
                        localcounter += 1  

            return localcounter 
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxarea = max(maxarea, bfs(row, col))  
        return maxarea 