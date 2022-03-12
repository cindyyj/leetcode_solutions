class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 有效的数独满足以下三个条件：
        # 同一个数字在每一行只能出现一次；
        # 同一个数字在每一列只能出现一次；
        # 同一个数字在每一个小九宫格只能出现一次。
        
        # https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
        # StefanPochmann
        
        N = 9 
        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]
        
        for r in range(N):
            for c in range(N):
                
                val = board[r][c]
                if val == '.':
                    continue
                
                box_idx = (r // 3) * 3 + c // 3
                
                if any([
                    val in rows[r],
                    val in cols[c], 
                    val in boxes[box_idx]
                ]):
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
        
        return True                