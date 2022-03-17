class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      
        m, n = len(grid), len(grid[0])
        q = collections.deque()
        
        t = 0
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    q.append((r, c, t))
                    
        def move(i, j):
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for di, dj in dirs:
                if 0 <= i + di < m and 0 <= j + dj < n:
                    yield i + di, j + dj
                    
        while q:
            r, c, t = q.popleft()
            for nr, nc in move(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, t + 1))
                    
        if any(1 in row for row in grid):
            return -1
        return t