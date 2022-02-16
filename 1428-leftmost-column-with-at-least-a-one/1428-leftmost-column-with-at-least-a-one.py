# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class binaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Start at Top Right, Move Only Left and Down
        # Start in the top right corner, and if the current value is a 0, move down. If it is a 1, then move left.
        
        m, n = binaryMatrix.dimensions()
        
        r, c = 0, n - 1
        
        # search grid 
        # When we encounter a 0, we know that the leftmost 1 can't be to the left of it.
        # we encounter a 1, we should continue the search on that row (move pointer to the left), in order to find an even smaller index.
        while r < m and c >= 0:
            if binaryMatrix.get(r, c) == 0:
                r += 1
            else:
                c -= 1
                
        return c + 1 if c != n - 1 else -1 
        
        


        