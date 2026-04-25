from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0 
        rows, cols = len(grid), len(grid[0])
        #up, down, left, right 
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def bfs(row, col):
            queue = deque()
            queue.append((row,col))
            grid[row][col] = 0 #show that it's visited  
            area = 1 

            while queue:
                r, c = queue.popleft()
                for dr,dc in directions: 
                    nr = dr + r
                    nc = dc + c 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        grid[nr][nc] = 0 
                        area += 1 
                
            return area 


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = bfs(row,col)
                    maxarea = max(area,maxarea) 
        return maxarea