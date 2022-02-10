class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # how many island? only one
        # check validity of the input, row, col grid[i][j] with other value? 
        
        rows, cols = len(grid), len(grid[0])
        p = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    p += 4
                    
                    if r > 0 and grid[r - 1][c] == 1:
                        p -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        p -= 2                    
        
        return p
        
        
        """
        Since we are traversing the grid from left to right, and from top to bottom, for each land cell we are currently at, we only need to check whether the LEFT and UP cells are land cells with a slight modification on previous approach.
        
        As you go through each cell on the grid, treat all the land cells as having a perimeter of 4 and add that up to the accumulated result.
        If that land cell has a neighboring land cell, remove 2 sides (one from each land cell) which will be touching between these two cells.
        If your current land cell has a UP land cell, subtract 2 from your accumulated result.
        If your current land cell has a LEFT land cell, subtract 2 from your accumulated result.
        """