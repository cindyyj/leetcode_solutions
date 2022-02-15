class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        tri = [[1] * (n + 1) for n in range(rowIndex + 1) ]
        
        for i in range(rowIndex + 1):
            for j in range(1, i):
                tri[i][j] = tri[i-1][j] + tri[i-1][j-1]
        
        return tri[rowIndex]
        