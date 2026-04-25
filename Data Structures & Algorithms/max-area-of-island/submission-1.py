from collections import deque 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxarea = 0 
        def bfs(row, col):
            directions = [(0,1), (0,-1), (1,0), (-1,0)] 
            queue = deque() 
            queue.append((row,col))
            grid[row][col] = 0
            counter = 0 
            while queue:
                row, col = queue.popleft() 
                counter += 1 
                for dr, dc in directions:
                    nr = dr + row 
                    nc = dc + col 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: 
                        queue.append((nr, nc))
                        grid[nr][nc] = 0 
                         
            return counter 

        for row in range(rows):
            for col in range(cols): 
                if grid[row][col] == 1:
                    maxarea = max(maxarea, bfs(row, col))

        return maxarea 