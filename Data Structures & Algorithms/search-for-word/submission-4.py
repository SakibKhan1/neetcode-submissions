class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[i] or
                (r, c) in path):
                return False

            path.add((r, c))

            for dr, dc in directions:
                nr = r + dr 
                nc = c + dc 
                if dfs(nr, nc, i + 1) == True:
                    path.remove((r, c))
                    return True
                

            path.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
