class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        
        def backtrack(row, col, i):
            temp = board[row][col]
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[i]:
                return False 
            if i == len(word) - 1: 
                return True 
            board[row][col] = '#'
            found = (
            backtrack(row + 1, col, i + 1) or
            backtrack(row - 1, col, i + 1) or 
            backtrack(row, col + 1, i + 1) or
            backtrack(row, col - 1, i + 1) 
            )

            board[row][col] = temp 
            return found  
            

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0):  # pass index 0
                        return True
        return False
