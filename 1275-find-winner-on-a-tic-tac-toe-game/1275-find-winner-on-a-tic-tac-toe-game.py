class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        
        board = [[0] * n for _ in range(n)]
        players = [1, -1]
        for i, (x, y) in enumerate(moves):
            player = players[i % 2]
            board[x][y] = player
            rows[x] += player
            cols[y] += player
            
            if x == y:
                diag += player
            
            if x + y == n - 1:
                anti_diag += player
        
            if any(abs(line) == n for line in [rows[x], cols[y], diag, anti_diag]):
                return "A" if player == 1 else "B"
        
        return "Draw" if len(moves) == n * n else "Pending"