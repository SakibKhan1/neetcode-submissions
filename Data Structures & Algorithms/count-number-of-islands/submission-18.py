from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        counter = 0 
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def bfs(row, col): 
            queue = deque()
            queue.append((row, col))
            grid[row][col] = "0"
            while queue:
                row, col = queue.popleft() 
                for dr, dc in directions:
                    nr = dr + row
                    nc = dc + col 
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == "1":
                        queue.append((nr,nc)) 
                        grid[nr][nc] = "0"


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col) 
                    counter += 1 

        return counter 