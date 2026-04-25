from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandcounter = 0
        rows, cols = len(grid), len(grid[0])
        #up, down, left, right  
        directions = [(-1,0), (+1, 0), (0, -1), (0,+1)]

        def bfs(row, col): 
            queue = deque() 
            queue.append((row,col))
            
            grid[row][col] = "0"
            while queue: 
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = dr + row 
                    nc = dc + col 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0" 
                        queue.append((nr,nc))

        for row in range(rows):
            for col in range(cols):
                #we only do bfs/dfs in the situation that we see a "1"
                if grid[row][col] == "1":
                    bfs(row, col) 
                    islandcounter += 1 
        return islandcounter 

