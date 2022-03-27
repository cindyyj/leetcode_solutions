class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        strengths = [(sum(row), i) for i, row in enumerate(mat)]
        
        # sort by numbers of soldiers and row index
        strengths.sort()
        return [i for _, i in strengths[:k]]