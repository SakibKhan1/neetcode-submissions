from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        # Define directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"  # Mark as visited

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1"):
                        queue.append((nr, nc))
                        grid[nr][nc] = "0"  # Mark as visited

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands