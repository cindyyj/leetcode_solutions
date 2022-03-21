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
        
        copy_board = [[board[row][col] for col in range(n)] for row in range(m)]
        
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