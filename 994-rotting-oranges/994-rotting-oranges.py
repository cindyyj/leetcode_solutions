class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()
        
        fresh = 0
        time = 0
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c, time))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q:
            i, j, time = q.popleft()
            for di, dj in dirs:
                if 0 <= i + di < m and 0 <= j+dj < n and grid[i+di][j+dj] == 1:
                    grid[i+di][j+dj] = 2
                    q.append((i+di, j+dj, time + 1))
                    
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:  
                    return -1
        
        return time
            