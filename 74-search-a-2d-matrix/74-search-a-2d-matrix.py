class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Brute Force
        # https://leetcode-cn.com/problems/search-a-2d-matrix/solution/fu-xue-ming-zhu-liu-chong-fang-fa-bang-n-e20z/
        
        # return any([target in row for row in matrix])
        
        # search from upper right or bottom left
        rows = len(matrix)
        cols = len(matrix[0])
        
        row, col = 0, cols-1
        
        while True:
            if row < rows and col >=0:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    col -= 1
                else:
                    row += 1
                    
            else:
                return False       
        