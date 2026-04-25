from collections import deque 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows = len(board)
        cols = len(board[0])
        visited = set() 

        def bfs(row, col):
            queue = deque() 
            queue.append((row,col))
            touches_edge = False
            region = [(row, col)]
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            while queue: 
                row, col = queue.popleft() 
                if (row == 0 or col == 0 or row == rows - 1 or col == cols - 1):
                    touches_edge = True 

                for dr, dc in directions:
                    nr = dr + row 
                    nc = dc + col 
                    if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O" and (nr, nc) not in visited:
                        visited.add((nr,nc))
                        region.append((nr,nc))
                        queue.append((nr,nc))
                        
            if not touches_edge:
                for row, col in region:
                    board[row][col] = "X" 
                


        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if board[row][col] == "O" and (row, col) not in visited:
                    bfs(row, col) 