class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        m, n = len(image), len(image[0])
        orig_color = image[sr][sc]
        if orig_color == newColor:
            return image
        
        def dfs(i, j):
            if not ((0 <= i < m) and (0 <= j < n)) or image[i][j] != orig_color:
                return
            
            image[i][j] = newColor
            
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dx, dy in dirs:
                dfs(i + dx, j + dy)
                
        dfs(sr, sc)
        return image          
            