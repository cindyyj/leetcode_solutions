class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return 
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                board[r][c] = "A" # connected to 'O'       
                # map is lazy function in python3
                # Many functions become "lazy" in python3, but list can call the iterator to make them work out.
                list(map(dfs, [r + 1, r - 1, r, r], [c, c, c + 1, c - 1]))            
        
        # mark Os connected to board O
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "A": 
                    board[r][c] = "O"
                elif board[r][c] == "O": 
                    board[r][c] = "X"           
        