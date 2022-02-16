import numpy as np

class Solution:
    def calculateEntropy(self, input: List[int]) -> float:
        
        if len(set(input)) <= 1:
            return 0
        value,counts = np.unique(input, return_counts=True)
        norm_counts = counts / counts.sum()
        return -sum(norm_counts * np.log2(norm_counts))