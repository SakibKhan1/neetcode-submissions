class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandcounter = 0 
        rows, cols = len(grid), len(grid[0])
        #up, down, left,right 
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != "1":
                return 
            grid[row][col] = "0" 
            
            for dr, dc in directions:
                nr = dr + row
                nc = dc + col 
                dfs(nr, nc) 



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1": 
                    dfs(row,col)
                    islandcounter += 1 
    

        return islandcounter  