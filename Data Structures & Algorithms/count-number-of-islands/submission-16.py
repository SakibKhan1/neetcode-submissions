from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0 
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(row, col): 
            queue = deque([(row, col)])
            grid[row][col] = "0"
            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc 
                    if nr < 0 or nc < 0 or nr>= rows or nc >= cols or grid[nr][nc] == "0":
                        continue
                    if grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        grid[nr][nc] = "0"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row, col)
                    counter += 1
        return counter 