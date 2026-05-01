from collections import deque 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def bfs(sr, sc):
            q = deque()
            q.append((sr,sc))
            region = [(sr, sc)]
            visited.add((sr, sc))
            touches_border = False

            while q:
                r, c = q.popleft()
                # if this cell is on the border, mark the region as safe
                if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                    touches_border = True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        region.append((nr, nc))

            # if region never touched the border → flip them
            if not touches_border:
                for r, c in region:
                    board[r][c] = "X"

        # 1. loop over every non-edge cell
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if board[r][c] == "O":
                    bfs(r, c)