from collections import deque
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        counter = 0 

        def bfs(row, col):
            nonlocal counter
            queue = deque()
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            queue.append((row, col))
            grid[row][col] = 2  # mark visited

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        counter += 1
                    elif grid[nr][nc] == 0:
                        counter += 1
                    elif grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # mark visited
                        queue.append((nr, nc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    bfs(row, col)
                    return counter  # only one island

        return counter
