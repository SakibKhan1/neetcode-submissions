from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))
        counter = 1
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue: 
            for _ in range(len(queue)):
                row, col = queue.popleft() 
                for dr,dc in directions:
                    nr = row + dr 
                    nc = col + dc 
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = counter  
                        queue.append((nr,nc))

            counter += 1 