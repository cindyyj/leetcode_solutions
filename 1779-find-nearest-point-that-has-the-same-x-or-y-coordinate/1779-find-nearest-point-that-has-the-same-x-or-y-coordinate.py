class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        """
        simplication of manhanttan distance abs(dx) + abs(dy) instead of abs(dx + dy) or abs(dx or dy).
        as already established that at least one of them is zero, might as well take advantage of that.
        """
        idx, smallest = -1, float('inf')
        
        for i, (a, b) in enumerate(points):
            dx, dy = a - x, b -  y
            if dx * dy == 0 and abs(dx + dy) < smallest:
                smallest = abs(dx + dy) 
                idx = i
        
        return idx 