from copy import copy, deepcopy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def get_neighbor(r, c):
            neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
            for dr, dc in neighbors:
                if 0 <= r + dr < m and 0 <= c + dc < n:
                    yield r + dr, c + dc
        
        
        m, n = len(board), len(board[0])
        
        copy_board = deepcopy(board)
        # copy_board = [[board[row][col] for col in range(n)] for row in range(m)]
        
        for r in range(m):
            for c in range(n):
                
                live = 0
                for nr, nc in get_neighbor(r, c):
                    if copy_board[nr][nc] == 1:
                        live += 1
                
                if copy_board[r][c] == 1 and (live < 2 or live > 3):
                    board[r][c] = 0
                
                if copy_board[r][c] == 0 and live == 3:
                    board[r][c] = 1
                    
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