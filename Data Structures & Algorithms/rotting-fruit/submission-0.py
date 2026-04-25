from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Scan the grid to find all rotten oranges and count fresh ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        def bfs(queue, fresh_count):
            time = 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue and fresh_count > 0:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append((nr, nc))
                            fresh_count -= 1
                time += 1

            return time if fresh_count == 0 else -1

        return bfs(q, fresh)