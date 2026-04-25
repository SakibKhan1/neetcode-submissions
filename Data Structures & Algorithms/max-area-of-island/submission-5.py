class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0 

        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col): 
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == 0: 
                return 0 

            grid[row][col] = 0 
            counter = 1

            for dr, dc in directions:
                nr = dr + row 
                nc = dc + col 
                counter += dfs(nr,nc) 

            return counter 


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1: 
                    maxarea = max(maxarea, dfs(row, col))

        return maxarea 