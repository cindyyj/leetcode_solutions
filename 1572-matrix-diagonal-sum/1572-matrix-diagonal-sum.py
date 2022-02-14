class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        diag1 = sum(mat[r][r] for r in range(n))
        diag2 = sum(mat[r][n - 1 - r] for r in range(n))
        
        if n % 2 == 1:
            return diag1 + diag2 - mat[n // 2][n // 2]
        else:
            return diag1 + diag2