import numpy as np

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat_list = []
        matrix = []

        for sublist in nums:
            for item in sublist:
                flat_list.append(item)

        if len(flat_list) != r * c:
            return nums
        else:
            for i in range(0,len(flat_list),c):
                matrix.append(flat_list[i:i+c])
            return matrix    
        
        # https://leetcode.com/problems/reshape-the-matrix/discuss/1317320/Python-One-Line-Two-Line-Yield-Generator-Circular-Index-Numpy-with-explaination(556)
        # generator expression (also called a generator comprehension), which has a very similar syntax to list comprehensions
        gen = (val for row in mat for val in row)
        return [[next(gen) for _ in range(c)] for _ in range(r)] if len(mat) * len(mat[0]) == r * c else mat        
    
        # # numpy
        # try:
        #     return np.array(mat).reshape(r, c)
        # except:
        #     return mat
        
        
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
        