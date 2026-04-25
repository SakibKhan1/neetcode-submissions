class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0 
        #up, down, left, right 
        directions = [(-1,0), (+1, 0), (0,-1), (0,+1)]
        rows, cols = len(grid), len(grid[0])

        def dfs(row,col):
            #base case is when it's out of bounds or it just doesn't equal 1 
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] != "1":
                return 
            grid[row][col] = "0"
            for dr,dc in directions:
                nr = dr + row 
                nc = dc + col 
                dfs(nr,nc) 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row,col)
                    res += 1 
        return res 