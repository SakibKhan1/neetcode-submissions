class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        res = [] 

        def backtrack(row, col, i): 
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != word[i]:
                return False 
            if i == len(word) - 1: 
                return True 

            temp = board[row][col] 
            board[row][col] = "#"

            bool_val = (
                backtrack(row + 1, col, i + 1) or
                backtrack(row - 1, col, i + 1) or 
                backtrack(row, col + 1, i + 1) or 
                backtrack(row, col - 1, i + 1) 

            )
            board[row][col] = temp 

            if bool_val == True:
                return True 
            else:
                return False 



        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(row, col, 0) == True:
                        return True 

        return False 