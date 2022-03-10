class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        """
        本题是一道非常经典且历史悠久的动态规划题，其作为算法题出现，
        最早可以追溯到 1994 年的 IOI（国际信息学奥林匹克竞赛）的 The Triangle。
        时光飞逝，经过 20 多年的沉淀，往日的国际竞赛题如今已经变成了动态规划的入门必做题，不断督促着我们学习和巩固算法。

        在本题中，给定的三角形的行数为 n，并且第 i 行（从 0 开始编号）包含了 i+1 个数。
        如果将每一行的左端对齐，那么会形成一个等腰直角三角形，如下所示：
        
        相邻结点：与(i, j) 点相邻的结点为 (i + 1, j) 和 (i + 1, j + 1)。
        
        dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        
        2 edge cases:
        - 第一列需要单独计算
        - 三角形斜边需要单独计算
        
        作者：LeetCode-Solution
        链接：https://leetcode-cn.com/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/
        作者：wang_ni_ma        
        链接：https://leetcode-cn.com/problems/triangle/solution/san-chong-jie-fa-duo-tu-xiang-jie-120-san-jiao-xin/

        """
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        
        return min(f[n - 1])     