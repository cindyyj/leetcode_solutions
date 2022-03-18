class Solution:
    def numIslands(self, grid):
        # https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
        # StefanPochmann
        """
        Hi, if you can't run the python code correctly, alter this part list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))).
        In python3, map return an iterator, which means, technically, it doesn't really compute the result (invoke the function) until you use it.
        So the original code in python3 just counts the number of '1', instead of DFS searching.
        Many functions become "lazy" in python3, but list can call the iterator to make them work out.
        """      
        
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


#     def numIslands(self, grid: List[List[str]]) -> int:
        
#         if not grid:
#             return 0
        
#         rows, cols = len(grid), len(grid[0])
        
#         def sink(r, c):
#             if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
#                 grid[r][c] = '0'
#                 map(sink, (r+1, r-1, r, r), (c, c, c+1, c-1))
                
#                 # beautiful example of map !!!
#                 # sink connected isaland

#                 # sink(r + 1, c)
#                 # sink(r - 1, c)
#                 # sink(r, c + 1)
#                 # sink(r, c - 1)
                
#                 return 1
#             return 0
        
#         cnt = 0
#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == '1':
#                     sink(r, c)
#                     cnt += 1
#         return cnt
        
        # return sum(sink(r, c) for r in range(rows) for c in range(cols))
    
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     def sink(i, j):
    #         if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
    #             grid[i][j] = '0'
    #             map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
    #             return 1
    #         return 0
    # return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
    
#首先明确岛屿定义：四周环海的独立陆地或者四周环海的连续陆地(连续的定义是上下左右方向也存在陆地)
#深度遍历的网格搜索。类似于二叉树的深度遍历递归。
#二叉树的深度遍历搜索的base case通常是非叶子结点即返回，而网格深度遍历搜索的返回条件是当越界情况出现时
#二叉树的递归是其左右孩子结点，而网格的递归是上下左右四个方向。
#唯一不同之处在于：网格的递归需要将走过的路进行标记，不然上下左右四个方向存在“回头路”的情况
#首先将当前访问结点置为“0”，表示已访问过
#找到第一个陆地，以它为根据地上下左右四个方向进行扩张，将所有访问过的与它相连的陆地全部用递归函数标记为0，直到上下左右不存在相连陆地的时候，我们将其陆地数量+1