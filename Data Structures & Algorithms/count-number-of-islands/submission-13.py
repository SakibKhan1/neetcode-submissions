from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0 
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col): 
            queue = deque()
            queue.append((row, col))
            grid[row][col] = "0" 

            while queue:
                directions = [(0,1), (0,-1), (1,0), (-1,0)]
                row, col = queue.popleft() 
                for dr, dc in directions: 
                    nr = dr + row 
                    nc = dc + col 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "0" 


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col) 
                    counter += 1 

        return counter 