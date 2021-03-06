class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # https://leetcode.com/problems/spiral-matrix-ii/discuss/1468207/Python-Smart-Simulate-by-marking-as-Visited-Clean-and-Concise
        # https://leetcode.com/problems/spiral-matrix-ii/discuss/22443/9-lines-python-solution
        
        res = [[0] * n for _ in range(n)]
        pos = [[(i, j) for j in range(n)] for i in range(n)]
        
        cnt = 1
        while pos:
            row = pos.pop(0)
            for x, y in row:
                res[x][y] = cnt
                cnt += 1
            pos = [*zip(*pos)][::-1]
        
        return res
        
        
        
        
#         ans = [[0] * n for _ in range(n)]
        
#         dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]] #(r + DIR[d][0], c + DIR[d][1]) corresponding to move [RIGHT, DOWN, LEFT, TOP]
#         r, c, d = 0, 0, 0
        
#         for i in range(1, n * n + 1):
#             # next r, next c
#             nr, nc = r + dirs[d][0], c + dirs[d][1]
#             if not 0 <= nr < n or not 0 <= nc < n or ans[nr][nc] != 0: # If out of bound or already visited, change directions
#                 d = (d + 1) % 4
#                 nr, nc = r + dirs[d][0], c + dirs[d][1]
                
#             ans[r][c] = i
#             r, c = nr, nc
            
#         return ans