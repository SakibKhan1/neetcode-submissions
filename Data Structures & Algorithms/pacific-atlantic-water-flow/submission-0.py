class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        pacific = set()
        atlantic = set()

        def bfs(starts, visited):
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and 0 <= nc < cols and
                        (nr, nc) not in visited and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        # Start BFS from Pacific edges
        pacific_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        for cell in pacific_starts:
            pacific.add(cell)
        bfs(pacific_starts, pacific)

        # Start BFS from Atlantic edges
        atlantic_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]
        for cell in atlantic_starts:
            atlantic.add(cell)
        bfs(atlantic_starts, atlantic)

        # Return intersection of both sets
        return list(pacific & atlantic)