class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def move(x, y):
            for i, j in ((1,0), (-1, 0), (0, 1), (0, -1)):
                if 0<= x + i < m and 0<= y+j < n:
                    yield x+i, y+j
        
        def dfs(x,y, index):
            area = 0
            grid[x][y] = index
            for i, j in move(x,y):
                if grid[i][j] == 1:
                    area += dfs(i, j, index)
            return area + 1
    
        # DFS every island and give it an index of island, get area of each island
        index = 2 # 0 ocean, 1 unvisited island
        areas = {0: 0}
        for x, y in product(range(m), range(n)):
            if grid[x][y] == 1:
                areas[index] = dfs(x,y, index)
                index += 1
        
        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for x, y in product(range(m), range(n)):
            if grid[x][y] == 0:
                seen = set(grid[i][j] for i, j in move(x,y))
                res = max(res, sum(areas[index] for index in seen) + 1)
                
        return res