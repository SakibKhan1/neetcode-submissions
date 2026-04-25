from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #so we count the freshfruits and then we put the rotten in the queue for bfs 
        freshfruits = 0 
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        counter = 0 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    freshfruits += 1 
                elif grid[row][col] == 2:
                    queue.append((row,col))

        while freshfruits > 0 and queue:
            for _ in range(len(queue)):
                directions = [(1,0), (-1,0), (0,1), (0,-1)]
                row, col = queue.popleft() 
                grid[row][col] = 2
                for dr, dc in directions:
                    nr = dr + row 
                    nc = dc + col 
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 
                        freshfruits -= 1 
                        queue.append((nr,nc)) 


            counter += 1 

        return counter if freshfruits == 0 else -1 