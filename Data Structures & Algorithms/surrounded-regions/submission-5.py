class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        rows, cols = len(board), len(board[0])
        def bfs(row, col):
            queue = deque()

            queue.append((row,col))
            board[row][col] = "T"
            while queue: 
                row, col = queue.popleft()
                for dr,dc in directions: 
                    nr = dr + row 
                    nc = dc + col 
                    if nc < 0 or nr < 0 or nr >= rows or nc >= cols or board[nr][nc] != "O":
                        continue 
                    board[nr][nc] = "T" 
                    queue.append((nr,nc))

        for row in range(rows):
            for col in range(cols): 
                if (row == 0 or row == rows - 1 or col == 0 or col == cols -1) and board[row][col] == "O":
                    bfs(row, col) 

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "T":
                    board[row][col] = "O" 
                elif board[row][col] == "O":
                    board[row][col] = "X"