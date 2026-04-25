from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        boxDict = defaultdict(set) 

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                boxKey = (row // 3, col // 3)
                if val == ".":
                    continue 
                elif (val in rowDict[row] or val in colDict[col] or 
                val in boxDict[boxKey]):
                    return False 
                rowDict[row].add(val)
                colDict[col].add(val) 
                boxDict[boxKey].add(val)
        return True 


