class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

#         def getNeighbors(row, col):
#             for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
#                 r, c = row + i, col + j
#                 if 0 <= r < m and 0 <= c < n:
#                     # yield is what makes a generator
#                     yield r, c
        
#         def bfs(row, col):
#             visited = set()
#             q = collections.deque([(row, col, 0)])
#             while q:
#                 x, y, d = q.popleft()
#                 for r, c in getNeighbors(x, y):
#                     if grid[r][c] == 0 and (r, c) not in visited:
#                         visited.add((r, c))
#                         distance[(r, c)].append(d+1)
#                         q.append((r, c, d+1))
                        
#         m, n = len(grid), len(grid[0])
#         distance = defaultdict(list)
#         building_count = 0
        
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     building_count += 1
#                     bfs(i, j)
                    
#         minimum = float('inf')
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     if (i, j) in distance and len(distance[(i, j)]) == building_count:
#                         minimum = min(minimum, sum(distance[(i, j)]))
        
#         return minimum if minimum != float('inf') else -1
    
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        total_sum = [[0] * cols for _ in range(rows)]
        
        def bfs(row, col, curr_count):
            min_distance = math.inf
            queue = deque()
            queue.append([row, col, 0])
            while queue:
                curr_row, curr_col, curr_step = queue.popleft()
                for d in dirs:
                    next_row = curr_row + d[0]
                    next_col = curr_col + d[1]
                    if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] == -curr_count:
                        total_sum[next_row][next_col] += curr_step + 1
                        min_distance = min(min_distance, total_sum[next_row][next_col])
                        grid[next_row][next_col] -= 1
                        queue.append([next_row, next_col, curr_step + 1])
            return min_distance
                
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    min_distance = bfs(row, col, count)
                    count += 1
                    if min_distance == math.inf:
                        return -1
        
        return min_distance