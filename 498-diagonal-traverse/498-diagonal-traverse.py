class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        m, n = len(mat), len(mat[0])
        
        if not m or not n:
            return []
        
        d = defaultdict(list)
        
        # i + j == 0, 1, ... , m + n - 1
        for r in range(m):
            for c in range(n):
                d[r + c].append(mat[r][c])
        
        ans = []
        for k, diag in d.items():
            if k % 2 == 0:
                ans += diag[::-1]
            else:
                ans += diag
                
        return ans