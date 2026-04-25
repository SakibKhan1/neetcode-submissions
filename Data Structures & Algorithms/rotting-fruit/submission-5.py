from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshfruits = 0 
        queue = deque() 
        res = 0 

        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    freshfruits += 1
                elif grid[row][col] == 2:
                    queue.append((row,col))
        directions = [(1,0),(-1,0),(0,1), (0,-1)]
        while freshfruits > 0 and queue: 
            for _ in range(len(queue)):
                row, col = queue.popleft() 
                for dr, dc in directions:
                    nr = row + dr 
                    nc = col + dc 
                    if 0 <= nr and 0 <= nc and nr < rows and nc < cols and grid[nr][nc] == 1:
                        freshfruits -= 1 
                        grid[nr][nc] = 2 
                        queue.append((nr,nc)) 

            res += 1 

        if freshfruits == 0:
            return res  
        else:
            return -1 