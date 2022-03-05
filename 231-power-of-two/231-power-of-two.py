class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        
        
        
        # power of 2, just has one 1-bit
        # n & (n-1) sets 1-bit to zero.  n - 1: change rightmost 1-bit to 0 and all lower bits to 1
        # turn off rightmost 1-bit 
        if n == 0:
            return False
        return n & (n - 1) == 0
    
    
#     # n in range of -2**31 <= n <= 2**31 - 1
#     BIG = 2**30

#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and Solution.BIG % n == 0
    
    