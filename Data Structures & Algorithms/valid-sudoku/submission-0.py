from collections import defaultdict 
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdict = defaultdict(set) #key will be row # and the values will be a set of contained values  
        coldict = defaultdict(set) #key will be col # and values are set of values  
        squaredict = defaultdict(set) #key will be row# and col# and // 3 for both 

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue 
                
                if (board[row][col] in rowdict[row] or 
                board[row][col] in coldict[col] or 
                board[row][col] in squaredict[(row // 3, col // 3)]):
                    return False 

                rowdict[row].add(board[row][col]) 
                coldict[col].add(board[row][col])
                squaredict[(row // 3, col // 3)].add(board[row][col])

        return True 


