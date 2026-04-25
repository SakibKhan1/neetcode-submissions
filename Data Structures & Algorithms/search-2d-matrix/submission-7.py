class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top, bottom = 0, rows - 1 

        while top <= bottom: 
            middle = (top + bottom) // 2 

            if target < matrix[middle][0]:
                bottom = middle - 1 

            elif target > matrix[middle][-1]:
                top = middle + 1 

            else:
                break 
        if not (top <= bottom):
            return False 

        left, right = 0, cols - 1 
        midrow = (top + bottom) // 2 

        while left <= right: 
            middle = (left + right) // 2 

            if target == matrix[midrow][middle]: 
                return True  
            
            elif target < matrix[midrow][middle]:
                right = middle - 1 
            
            else:
                left = middle + 1 

        return False 