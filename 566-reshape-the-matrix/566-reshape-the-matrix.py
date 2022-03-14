import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        # https://leetcode.com/problems/reshape-the-matrix/discuss/1317320/Python-One-Line-Two-Line-Yield-Generator-Circular-Index-Numpy-with-explaination(556)
        # numpy
        try:
            return np.array(mat).reshape(r, c)
        except:
            return mat
        
        
#         # matrix[index / width][index % width] for both the input and the output matrix.
#         m, n = len(mat), len(mat[0])
        
#         # invalid
#         if r * c != m * n: 
#             return mat
        
#         new = [[0] * c for _ in range(r)]
#         for i in range(m*n):
#             new[i // c][i % c] = mat[i // n][i % n]        
#         return new
            
        
        # return np.array(mat).reshape(r, c)
        