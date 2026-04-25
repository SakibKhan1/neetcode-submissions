class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0 
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return 

            grid[row][col] = "0" 
            for dr, dc in directions:
                nr = dr + row 
                nc = dc + col 
                dfs(nr, nc)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col) 
                    counter += 1 

        return counter 