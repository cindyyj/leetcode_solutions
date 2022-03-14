class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        row, col = len(maze), len(maze[0])
        if not maze or not entrance:
            return -1
                
        def move(r, c):
            directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                # not outside maze, and not wall
                if 0 <= r + dx < row and 0 <= c + dy < col and maze[r + dx][c + dy] != "+":
                    yield r + dx, c + dy

        queue = deque()
        # (x, y, distance)
        x, y = entrance #entrance[0], entrance[1]
        queue.append((x, y, 0))
        maze[x][y] = "+"
        
        while queue:
            for _ in range(len(queue)):
                r, c, dist = queue.popleft()
                for nr, nc in move(r, c):
                    if nr in [0, row - 1] or nc in [0, col - 1]:
                        return dist + 1
                    else:
                        queue.append((nr, nc, dist + 1))
                        maze[nr][nc] = '+'
        return -1 
    
    