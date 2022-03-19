class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        if not m or not n:
            m = n = 0
        self.pres = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.pres[i + 1][j + 1] = matrix[i][j] + self.pres[i][j + 1] + self.pres[i + 1][j] - self.pres[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pres[row2 + 1][col2 + 1] - self.pres[row1][col2 + 1] - self.pres[row2 + 1][col1] + self.pres[row1][col1] 
        

# preSum[row2][col2]−preSum[row2][col1−1]−preSum[row1−1][col2]+preSum[row1−1][col1−1]
# 链接：https://leetcode-cn.com/problems/range-sum-query-2d-immutable/solution/ru-he-qiu-er-wei-de-qian-zhui-he-yi-ji-y-6c21/
# 每个顶点算一个值，m*n矩阵对应着(m + 1) * (n + 1)顶点，

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)