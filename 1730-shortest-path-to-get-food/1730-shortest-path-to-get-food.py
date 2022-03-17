class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        # DFS will be used when we need to find a path between two nodes.
        # (not necessarily shortest path . It may be shortest or longest path.)
        # BFS will be used when we need to find SHORTEST Path between two nodes
        
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '*':
                    q = collections.deque([])
                    q.append((r, c, 0))
                    grid[r][c] = 0
                    
                    while q:
                        r, c, dist = q.popleft()
                        for dr, dc in dirs:
                            nr = r + dr
                            nc = c + dc
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] in ('O', '#'):
                                if grid[nr][nc] == '#':
                                    return dist + 1
                                q.append((nr, nc, dist + 1))
                                grid[nr][nc] = 0
        
        return -1 