class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
# --------------------------- METHOD 1, Brute Force, one liner!  ---------------------------
        # https://leetcode-cn.com/problems/search-a-2d-matrix/solution/fu-xue-ming-zhu-liu-chong-fang-fa-bang-n-e20z/       
        return any([target in row for row in matrix])

# # --------------------------- METHOD 2, Binary Search  ---------------------------    
#         # binary search!!!, time O(log(mn))
#         m = len(matrix)
#         n = len(matrix[0])
        
#         if not m or not n:
#             return False
        
#         l, r = 0, m * n - 1
#         while l <= r:
#             mid = l + (r - l) // 2
#             val = matrix[mid // n][mid % n]
#             if val == target:
#                 return True
#             elif val < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
        
#         return False     

# --------------------------- METHOD 3, not recommend  ---------------------------        
#         # time complexity, O(mn), didn't take advantage of the sorted property! do not recommend
#         # search from upper right or bottom left
#         rows = len(matrix)
#         cols = len(matrix[0])
        
#         row, col = 0, cols-1
        
#         while True:
#             if row < rows and col >=0:
#                 if matrix[row][col] == target:
#                     return True
#                 elif matrix[row][col] > target:
#                     col -= 1
#                 else:
#                     row += 1
                    
#             else:
#                 return False       
        