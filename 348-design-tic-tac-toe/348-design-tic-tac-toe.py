class TicTacToe:
# Record the number of moves for each rows, columns, and two diagonals.
# For each move, we -1 for each player 1's move and +1 for player 2's move.
# Then we just need to check whether any of the recored numbers equal to n or -n.

    def __init__(self, n: int):
        self.row, self.col = [0] * n, [0] * n
        self.diag, self.anti_diag = 0, 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        
        # if player == 0:
        #     offset = -1
        # else: # player == 1
        #     offset = 1
        # offset = player * 2 - 3
        
        offset = 1 if player == 1 else -1
        
        self.row[row] += offset
        self.col[col] += offset
        
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        
        # since only the player currently playing has a chance to win
        if offset * self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return player
        
        return 0
        


# # Your TicTacToe object will be instantiated and called as such:
# # obj = TicTacToe(n)
# # param_1 = obj.move(row,col,player)