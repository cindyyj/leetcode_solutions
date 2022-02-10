class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def sink(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                grid[r][c] = 0
                
                # beautiful example of map !!!
                # sink connected isaland
                # map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                sink(r + 1, c)
                sink(r - 1, c)
                sink(r, c + 1)
                sink(r, c - 1)
                
                return 1
            return 0
        
        return sum(sink(r, c) for r in range(rows) for c in range(cols))
    
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     def sink(i, j):
    #         if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
    #             grid[i][j] = '0'
    #             map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
    #             return 1
    #         return 0
    # return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))