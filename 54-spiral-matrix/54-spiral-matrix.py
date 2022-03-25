class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given that we are at (row, col), where row is the row index, and col is the column index.

        move right: (row, col + 1)
        move downwards: (row + 1, col)
        move left: (row, col - 1)
        move upwards: (row - 1, col)
        
          spiral_order([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

        = [1, 2, 3] + spiral_order([[6, 9],
                                    [5, 8],
                                    [4, 7]])

        = [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                             [5, 4]])

        = [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                                      [5]])

        = [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

        = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

        = [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

        = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        
        """
        # return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

        
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order
      
        
#         # simulation
#         if not matrix or not matrix[0]:
#             return list()
        
#         rows, columns = len(matrix), len(matrix[0])
#         order = list()
#         left, right, top, bottom = 0, columns - 1, 0, rows - 1
#         while left <= right and top <= bottom:
#             for column in range(left, right + 1):
#                 order.append(matrix[top][column])
#             for row in range(top + 1, bottom + 1):
#                 order.append(matrix[row][right])
#             if left < right and top < bottom:
#                 for column in range(right - 1, left, -1):
#                     order.append(matrix[bottom][column])
#                 for row in range(bottom, top, -1):
#                     order.append(matrix[row][left])
#             left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
#         return order

# # 作者：LeetCode-Solution
# # 链接：https://leetcode-cn.com/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode-solution/

        
#         m, n = len(matrix), len(matrix[0])
        
#         if not m or not n:
#             return list()
        
#         order = list()
#         left, right, top, bottom = 0, n - 1, 0, m - 1
#         while left <= right and top <= bottom:
#             for col in range(left, right + 1):
#                 order.append(matrix[top][col])
#             top += 1
#             if top > bottom:
#                 break
                
#             for row in range(top, bottom + 1):
#                 order.append(matrix[row][right])
#             right -= 1
#             if right < left:
#                 break
            
#             for col in range(right, left - 1, -1):
#                 order.append(matrix[bottom][col])
#             bottom -= 1
#             if bottom < top:
#                 break
            
#             for row in range(bottom, top - 1, -1):
#                 order.append(matrix[row][left])
#             left += 1
#             if left > right: break
        
#         return order                  