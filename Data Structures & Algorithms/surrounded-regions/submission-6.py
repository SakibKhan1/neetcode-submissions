class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or board[row][col] != "O":
                return 
            board[row][col] = "T"
            for dr,dc in directions:
                nr = row + dr 
                nc = dc + col 
                dfs(nr,nc)

        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == rows - 1 or col == 0 or col == cols - 1: 
                    dfs(row, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O": 
                    board[row][col] = "X" 
                elif board[row][col] == "T":
                    board[row][col] = "O"  
