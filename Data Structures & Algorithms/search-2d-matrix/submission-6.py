class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top, bot = 0, rows - 1 

        while top <= bot:
            midrow = (top + bot) // 2 
            if target > matrix[midrow][-1]:
                top = midrow + 1 
            elif target < matrix[midrow][0]:
                bot = midrow - 1 
            else:
                break
        if not (top <= bot):
            return False 

        left = 0 
        right = (cols - 1)
        midrow = (top + bot) // 2 
        while left <= right:
            midcol = (left + right) // 2 
            if target < matrix[midrow][midcol]:
                
                right = midcol - 1 
            elif target > matrix[midrow][midcol]:
                left = midcol + 1 
            else:
                return True 
        return False  