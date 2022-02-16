class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, cnt = 0, n - 1, 0
        while r < m and c >= 0:
            if grid[r][c] < 0:
                cnt += m - r
                c -= 1
            else:
                r += 1
        return cnt
    
    """

    ++++++
    ++++--
    ++++--
    +++---
    +-----
    +-----
    
    For more practice of similar problem, please refer to:
    240. Search a 2D Matrix II , -- credit to @cerb668.
    1428. Leftmost Column with at Least a One


    """