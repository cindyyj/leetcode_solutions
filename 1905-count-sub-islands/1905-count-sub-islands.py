class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        m, n = len(grid1), len(grid1[0])
        rows, cols = len(grid1), len(grid1[0])
        
        if not rows or not cols:
            return 0
        
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid2[r][c] == 1:
                # 赋值不要用 == 要用 =
                grid2[r][c] = 0 

                for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    dfs(r + dr, c + dc)
        

        # removing all the non-common sub-islands
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    # function calls, not use [], use ()
                    dfs(i, j)
        
        # count number of sub-islands
        cnt = 0 
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    cnt += 1
                    
        return cnt
        