class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        上下翻转
        然后再左上-右下对角条线为轴做翻转     
        
        先以左上-右下对角条线为轴做翻转；
        再以中心的竖线为轴做翻转
        """
        n = len(matrix)
             
        # reflect 水平翻转, 上下
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
   
        # transpose 主对角线翻转,  Reverse on Diagonal 
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
