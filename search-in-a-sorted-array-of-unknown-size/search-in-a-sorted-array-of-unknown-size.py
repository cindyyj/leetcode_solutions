# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        upper = 10**4 
        
        if reader.get(0) == target:
            return 0
        
        # search boundries
        l, r = 0, 1
        while reader.get(r) < target:
            l = r
            r <<= 1  # To speed up, use right shift instead of multiplication: right <<= 1. same as r *= 2
            
        r = max(r, upper)
        
        while l <= r:
            mid = l + ((r-l) >> 1)
            num = reader.get(mid)
            
            if num == target:
                return mid
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return -1             