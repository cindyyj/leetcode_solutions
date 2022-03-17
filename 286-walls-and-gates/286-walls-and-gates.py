class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        INF = 2**31 - 1
        q = collections.deque()
        m, n = len(rooms), len(rooms[0])
        
        def move(r, c):
            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            for dr, dc in dirs:
                if 0 <= r + dr < m and 0 <= c + dc < n:
                    yield r + dr, c + dc
        
        d = 0
        for r, row in enumerate(rooms):
            for c, val in enumerate(row):
                if val == 0:
                    q.append((r, c, d))
        
        while q:
            r, c, d = q.popleft()
            for nr, nc in move(r, c):
                if rooms[nr][nc] == INF:
                    rooms[nr][nc] = d + 1
                    q.append((nr, nc, d + 1))
                    
        return rooms