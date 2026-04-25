class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set() 
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(1,0), (0,-1), (-1,0)]
        def dfs(row, col, visited, prev):
            if (row < 0 or col < 0 or row >= rows or col >= cols or (row,col) in visited or heights[row][col] < prev):
                return 
            visited.add((row, col))
            for dr, dc in directions:
                nr = dr + row 
                nc = dc + col 
                dfs(nr, nc, visited, heights[row][col])


        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols - 1])

        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])
        res =[]
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac and (row, col) in atl: 
                    res.append([row, col])
        return res  