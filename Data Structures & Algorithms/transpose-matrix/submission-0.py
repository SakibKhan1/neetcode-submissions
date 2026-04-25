class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        newmatrix = [[0 for _ in range(rows)] for _ in range(cols)]

        r, c = len(newmatrix), len(newmatrix[0])


        for row in range(r):
            for col in range(c):
                newmatrix[row][col] = matrix[col][row]
                 

        return newmatrix 