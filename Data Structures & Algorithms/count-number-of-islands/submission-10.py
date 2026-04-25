from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0 
        #up, down, left, right 
        directions = [(-1,0), (+1, 0), (0,-1), (0,+1)]
        rows, cols = len(grid), len(grid[0])

        def bfs(row,col):
            queue = deque()
            queue.append((row,col))
            grid[row][col] = "0" #marking it as 0 makes it "visited"

            while queue: 
                row, col = queue.popleft() 
                for dr,dc in directions:
                    nr = row + dr 
                    nc = col + dc 
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "0" 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row,col)
                    res += 1 
        return res 