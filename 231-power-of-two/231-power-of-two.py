class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0
    
    
#     # n in range of -2**31 <= n <= 2**31 - 1
#     BIG = 2**30

#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and Solution.BIG % n == 0
    
    