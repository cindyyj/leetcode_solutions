import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:   
        
        # one-line
        return [original[i*n : (i + 1)*n] for i in range(m)] if m*n == len(original) else []
        
        
        # try:
        #     return np.array(original).reshape(m, n)
        # except:
        #     return []