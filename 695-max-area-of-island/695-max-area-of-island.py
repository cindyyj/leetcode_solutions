class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col]:
                grid[row][col] = 0
                return 1 + area(row - 1, col) + area(row + 1, col) + area(row, col - 1) + area(row, col + 1)
            return 0
        
        return max(area(r, c) 
                   for r in range(len(grid)) 
                   for c in range(len(grid[0])))
        
# 遍历二维数组，对于每块土地，去其前后左右找相邻土地，再去前后左右的土地找其前后左右的土地，直到周围没有土地
# 对于每一块已找过的土地，为避免重复计算，将其置为0
# 其实就是遍历了所有的岛屿，然后取这些岛屿的最大面积res = max(res, dfs(i, j))

# 作者：edelweisskoko
# 链接：https://leetcode-cn.com/problems/max-area-of-island/solution/695-dao-yu-de-zui-da-mian-ji-dfs-bfsshua-oe8m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。       



                