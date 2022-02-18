class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        ans = 0
        
        # edge cases
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        dirs = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        queue = collections.deque([(0,0,1)]) # row, col, path steps (distance)
        seen = set()
        seen.add((0,0))
        
        def getnext(row, col):
            for dx, dy in dirs:
                r, c = row + dx, col + dy
                if 0 <= r < n and 0 <= c < n:
                    yield r, c
        
        while queue:
            row, col, d = queue.popleft()
            if (row, col) == (n-1, n-1):
                return d
            for r, c in getnext(row, col):
                if (r, c) not in seen and grid[r][c] == 0:
                    seen.add((r,c))
                    queue.append((r, c, d+1))
        
        return -1 
        
  
        
        """
        You can recognize that this is a typical shortest path problem that can be solved with a Breadth-first search (BFS).
        You can correctly implement a BFS to solve it.
        For bonus points, you know that the solution could be optimized using the A* algorithm.
        """