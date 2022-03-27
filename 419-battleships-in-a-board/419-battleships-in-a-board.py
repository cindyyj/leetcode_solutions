class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        cnt = 0 
        
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == "X" and not ((i > 0 and board[i - 1][j] == 'X') or (j > 0 and board[i][j - 1] == 'X')):
                    cnt += 1
        return cnt
        
        """
        假设矩阵的行数为 \textit{row}row，矩阵的列数 \textit{col}col，矩阵中的位置 (i, j)(i,j) 为战舰的左上顶点，需满足以下条件：

        满足当前位置所在的值 \textit{board}[i][j] = \texttt{'X'}board[i][j]=’X’；
        满足当前位置的左则为空位，即\textit{board}[i][j-1] = \texttt{'.'}board[i][j−1]=’.’；
        满足当前位置的上方为空位，即\textit{board}[i-1][j] = \texttt{'.'}board[i−1][j]=’.’；
        我们统计出所有战舰的左上顶点的个数即为所有战舰的个数。

        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/battleships-in-a-board/solution/jia-ban-shang-de-zhan-jian-by-leetcode-s-kxpc/     
        """