from collections import deque
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(start_row, start_col):
            queue = deque()
            queue.append((start_row, start_col))
            grid[start_row][start_col] = 0  # mark visited
            perimeter = 0

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    # If out of bounds or water → exposed edge
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0:
                        perimeter += 1

                    # If unvisited land → BFS
                    elif grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 0  # mark visited

            return perimeter

        # Find the first land cell (only one island exists)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return bfs(row, col)
