from copy import copy, deepcopy
import numpy as np

class Solution:
    def gameOfLifeRule(self, live_cells):        
        cell_map = defaultdict(int)
        near = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        for row_num,col_num in live_cells:
            for dx,dy in near:
                i = row_num + dx
                j = col_num + dy
                if row_num != i or col_num != j:
                    cell_map[(i,j)] += 1
        
        # 细胞存活的规则为: 
        # 1. 活细胞周围有2,3个活细胞存活
        # 2. 死细胞周围有3个活细胞存活
        return {cell for cell in cell_map if (cell_map[cell] == 3 and cell not in live_cells)
                                        or (cell_map[cell] in (2, 3) and cell in live_cells)}


    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 初始的活细胞所在位置
        live_cells = {(i, j) for i, row in enumerate(board) for j, is_live in enumerate(row) if is_live}

        # 通过规则判断下一轮的活细胞所在位置
        live_cells = self.gameOfLifeRule(live_cells)

        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live_cells)
        
        
        
        """
        Do not return anything, modify board in-place instead.
        
        没有补零 (zero padding) 的2维卷积的示意图，
        深蓝色的 3 x 3 的正方形就是所说的 kernel，下面的浅蓝色就是图像，通过滑动 kernel 并且将 kernel 的对应位置和它覆盖区域的对应位置的数值相乘并加和，
        就可以得到卷积后某一个位置的值，大家可以自己看着图计算一下
        
        下图展示的是带 zero padding 的 2D 卷积操作，也是为了方便处理我们的数据
        (本题中同样采用补零，如果不在原始的 board 的周围补零，对于 board 最外围的一圈值处理起来比较麻烦，而通过补零我们可以统一进行处理)
        
        能想到卷积操作是相当厉害了，这里 * 就是利用了 numpy 中最朴素的逐位对应相乘。
        卷积核的作用是计数，所以中间位置是 0，周围 8 个位置是 1，乘积之和就是周围存活的生命数。
        顺便复习了卷积神经网络（CNN）的相关概念。
        
        """
# # 作者：LotusPanda
# # 链接：https://leetcode-cn.com/problems/game-of-life/solution/xiong-mao-shua-ti-python3-bao-xue-bao-hui-cvzhong-/

#         r, c = len(board), len(board[0])
#         # 下面两行做 zero padding
#         board_exp = np.array([[0 for _ in range(c + 2)] for _ in range(r + 2)])
#         board_exp[1:1 + r, 1:1 + c] = np.array(board)
#         # 设置卷积核
#         kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
#         # 开始卷积
#         for i in range(1, r + 1):
#             for j in range(1, c + 1):
#                 # 统计细胞周围 8 个位置的状态
#                 temp_sum = np.sum(kernel * board_exp[i - 1:i + 2, j - 1:j + 2])
#                 # 按照题目规则进行判断
#                 if board_exp[i, j] == 1:
#                     if temp_sum < 2 or temp_sum > 3:
#                         board[i - 1][j - 1] = 0
#                 else:
#                     if temp_sum == 3:
#                         board[i - 1][j - 1] = 1  


        
#         def get_neighbor(r, c):
#             neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
#             for dr, dc in neighbors:
#                 if 0 <= r + dr < m and 0 <= c + dc < n:
#                     yield r + dr, c + dc
        
        
#         m, n = len(board), len(board[0])
        
#         copy_board = deepcopy(board)
#         # copy_board = [[board[row][col] for col in range(n)] for row in range(m)]
        
#         for r in range(m):
#             for c in range(n):
                
#                 live = 0
#                 for nr, nc in get_neighbor(r, c):
#                     if copy_board[nr][nc] == 1:
#                         live += 1
                
#                 if copy_board[r][c] == 1 and (live < 2 or live > 3):
#                     board[r][c] = 0
                
#                 if copy_board[r][c] == 0 and live == 3:
#                     board[r][c] = 1
                    
        """
        一. 普遍意义上，如果规则极其繁复，如何简化这些规则呢？
        关于逻辑表达式的简化可能会用上“卡诺图”，有兴趣的朋友请自行查一查。
        
        二. 这道题的规则如何简化？

        1. 原来是活的，周围有2-3个活的，成为活的
        2. 原来是死的，周围有3个活的，成为活的
        3. 其他都是死了
        
        y = deepcopy(x)
        for 2D array of floats copy do not work, but deepcopy does work, thanks!
        copy() is not sufficient, it is a shallow copy so the result will be a copy of references to the original row lists. 
        """