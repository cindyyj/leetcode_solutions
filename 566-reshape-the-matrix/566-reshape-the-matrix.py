import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        if r * c != m * n:
            return mat
        
        return np.array(mat).reshape(r, c)
        