from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islandcounter = 0 
        #up, down, left, right 
        directions = ([-1,0], [+1,0], [0,-1], [0,+1])

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            grid[r][c] = "0" #shows it's marked as visited when given a "0" value 

            while queue: 
                row, col = queue.popleft() 
                for dr, dc in directions:
                    nr = row + dr 
                    nc = col + dc 
                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "0" 


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col) 
                    islandcounter += 1 
        return islandcounter 