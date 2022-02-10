class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # time complexity: O(R*C) , number of rows * number of columns
        # no island? 
        
        rows, cols = len(grid), len(grid[0])
        def area(r, c):
            # if island and index within grid
            if 0 <= r < rows and 0 <= c < cols and grid[r][c]:
                grid[r][c] = 0
                return (1 + 
                       area(r - 1, c) +
                       area(r + 1, c) +
                       area(r, c - 1) +
                       area(r, c + 1) 
                       )
            return 0
        
        maxarea = 0
        for r in range(rows):
            for c in range(cols):
                maxarea = max(maxarea, area(r, c))
                
        return maxarea
            
            
# # --------------------------- METHOD 1 ---------------------------
#     def inarea(self, grid, r, c):
#         return (0 <= r < len(grid)) and (0 <= c < len(grid[0]))
    
#     def area(self, grid, r, c):
#         if not self.inarea(grid, r, c):
#             return 0
        
#         if grid[r][c] != 1:
#             return 0
#         else: # grid[r][c] == 1
#             grid[r][c] = 2
            
#         return (1 + 
#                 self.area(grid, r - 1, c) + 
#                 self.area(grid, r + 1, c) + 
#                 self.area(grid, r, c - 1) + 
#                 self.area(grid, r, c + 1)               
#                )
        
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         maxarea = 0 
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 maxarea = max(maxarea, self.area(grid, r, c))
        
#         return maxarea
    
# # --------------------------- METHOD 2 ---------------------------    
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
#         # time complexity: O(R*C) , number of rows * number of columns
#         def area(row, col):
#             if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col]:
#                 # mark as visited
#                 grid[row][col] = 0
#                 return 1 + area(row - 1, col) + area(row + 1, col) + area(row, col - 1) + area(row, col + 1)
#             return 0
        
#         return max(area(r, c) 
#                    for r in range(len(grid)) 
#                    for c in range(len(grid[0])))
        
# 遍历二维数组，对于每块土地，去其前后左右找相邻土地，再去前后左右的土地找其前后左右的土地，直到周围没有土地
# 对于每一块已找过的土地，为避免重复计算，将其置为0
# 其实就是遍历了所有的岛屿，然后取这些岛屿的最大面积res = max(res, dfs(i, j))

# 作者：edelweisskoko
# 链接：https://leetcode-cn.com/problems/max-area-of-island/solution/695-dao-yu-de-zui-da-mian-ji-dfs-bfsshua-oe8m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。       



                