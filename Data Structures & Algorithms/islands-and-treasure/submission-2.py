from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()

        # Step 1: collect all treasure chests (0)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # Step 2: BFS with a layer counter
        counter = 0 
        while queue:
            size = len(queue)
            for _ in range(size):  # process one BFS layer
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == 2147483647 
                    ):
                        grid[nr][nc] = counter + 1 
                        queue.append((nr, nc))
            counter += 1
