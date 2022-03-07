class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given that we are at (row, col), where row is the row index, and col is the column index.

        move right: (row, col + 1)
        move downwards: (row + 1, col)
        move left: (row, col - 1)
        move upwards: (row - 1, col)
        """
        
        m, n = len(matrix), len(matrix[0])
        
        if not m or not n:
            return list()
        
        order = list()
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                order.append(matrix[top][col])
            top += 1
            if top > bottom:
                break
                
            for row in range(top, bottom + 1):
                order.append(matrix[row][right])
            right -= 1
            if right < left:
                break
            
            for col in range(right, left - 1, -1):
                order.append(matrix[bottom][col])
            bottom -= 1
            if bottom < top:
                break
            
            for row in range(bottom, top - 1, -1):
                order.append(matrix[row][left])
            left += 1
            if left > right: break
        
        return order                  