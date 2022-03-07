class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ROWS, self.COLS = len(board), len(board[0])
        self.board = board
        
        if not self.board or not self.ROWS or not self.COLS:
            return False
        
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.dfs(row, col, word, 0):  # pass index instead of passing word slicing to save space
                    return True
        
        return False
    
    def dfs(self, row, col, word, cur):
        if cur == len(word):
            return True
        
        if row < 0 or row >= self.ROWS or col < 0 or col >= self.COLS \
                or self.board[row][col] != word[cur]:
            return False
        
        res = 'False'
        self.board[row][col] = '#'
        
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            res = self.dfs(row + dr, col + dc, word, cur + 1)
            if res:
                break
                
        self.board[row][col] = word[cur]
        
        return res
        