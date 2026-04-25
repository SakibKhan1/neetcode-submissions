from collections import deque
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = set()

        def bfs(sr, sc):
            queue = deque([(sr, sc)])
            visited.add((sr, sc))
            perimeter = 0

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    # Out of bounds → perimeter
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        perimeter += 1

                    # Water → perimeter
                    elif grid[nr][nc] == 0:
                        perimeter += 1

                    # Unvisited land → BFS
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)
