class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        counter = 0 
        def bfs(row, col): 
            nonlocal counter 
            queue = deque()
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            queue.append((row,col))
            grid[row][col] = 2 

            while queue:
                row, col = queue.popleft() 
                for dr,dc in directions:
                    nr = dr + row 
                    nc = dc + col 
                    if nr >= 0 and nc >=0 and nr < rows and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 
                        queue.append((nr,nc))

                    elif nr >= 0 and nc >=0 and nr < rows and nc < cols and grid[nr][nc] == 0:
                        counter += 1 
                    elif nr < 0:
                        counter += 1 
                    elif nc < 0:
                        counter += 1 
                    elif nr >= rows:
                        counter += 1 
                    elif nc >= cols:
                        counter += 1 

        for row in range(rows):
            for col in range(cols): 
                if grid[row][col] == 1:
                    bfs(row,col)
                    return counter 

        return counter 

    
