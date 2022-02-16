class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # return any([target in r for r in matrix])
        
        rows, cols = len(matrix), len(matrix[0])

        if not rows or not cols:
            return False
        
        row, col = 0, cols-1
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return False