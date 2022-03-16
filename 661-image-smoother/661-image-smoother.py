class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        # rows, cols
        m, n = len(img), len(img[0])
        new = [[0]*n for _ in range(m)]
        
        for i in range(m*n):            
            r, c = i//n, i%n
            cnt = 0
            for nr in (r-1, r, r+1):
                for nc in (c-1, c, c+1):
                    if 0<= nr < m and 0 <= nc < n:
                        new[r][c] += img[nr][nc]
                        cnt += 1
            new[r][c] //= cnt         
            
        return new        