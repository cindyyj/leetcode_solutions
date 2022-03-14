class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        
        # https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
        # 2D dp, 2 pass: 
        # update based on its left and top neighbors;
        # then update based on its right and bottom neighbors.
        # 首先从左上角开始递推 是由其 「左方」和 「左上方」的最优子状态决定的；
        # 然后从右下角开始递推 是由其 「右方」和 「右下方」的最优子状态决定的；

        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat