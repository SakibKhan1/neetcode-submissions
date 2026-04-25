class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        zeroRow = False 

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0 
                    if row > 0: 
                        matrix[row][0] = 0 
                    else:
                        zeroRow = True 


        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0 

        if matrix[0][0] == 0:
            for row in range(rows):
                matrix[row][0] = 0 
        
        if zeroRow:
            for col in range(cols):
                matrix[0][col] = 0 