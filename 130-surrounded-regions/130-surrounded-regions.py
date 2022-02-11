           
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return 
        
        self.rows, self.cols = len(board), len(board[0])
        
        # Step 1). retrieve all border cells
        from itertools import product
        borders = (list(product(range(self.rows), [0, self.cols - 1])) + 
                    list(product([0, self.rows - 1], range(self.cols))))

        
        def dfs(board, r, c):
            if 0 <= r < self.rows and 0 <= c < self.cols and board[r][c] == "O":
                board[r][c] = "A" # connected to 'O'   
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dfs(board, r+dx, c+dy)
                
        # Step 2). mark the "escaped" cells, with any placeholder, e.g. 'E'
        for r, c in borders:
            self.dfs(board, r, c)
            
        # Step 3). flip the captured cells ('O'->'X') and the escaped one ('E'->'O')
        
        for r in range(self.rows):
            for c in range(self.cols):
                if board[r][c] == "O":   board[r][c] = "X"
                elif board[r][c] == "A": board[r][c] = "O"

    def dfs(self, board, r, c):
        if 0 <= r < self.rows and 0 <= c < self.cols and board[r][c] == "O":
            board[r][c] = "A" # connected to 'O'   
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                self.dfs(board, r+dx, c+dy)


#         if not board:
#             return 
        
#         rows, cols = len(board), len(board[0])
        
#         def dfs(r, c):
#             if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
#                 board[r][c] = "A" # connected to 'O'       
#                 # map is lazy function in python3
#                 # Many functions become "lazy" in python3, but list can call the iterator to make them work out.
#                 list(map(dfs, [r + 1, r - 1, r, r], [c, c, c + 1, c - 1]))            
        
#         # mark Os connected to board O
#         for r in range(rows):
#             dfs(r, 0)
#             dfs(r, cols - 1)
        
#         for c in range(cols):
#             dfs(0, c)
#             dfs(rows - 1, c)
            
#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == "A": 
#                     board[r][c] = "O"
#                 elif board[r][c] == "O": 
#                     board[r][c] = "X"           
        