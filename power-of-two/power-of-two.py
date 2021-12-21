class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # if n <= 0:
        #     return False
        # elif n == 1:
        #     return True
        # else:
        #     while n / 2 >= 1:
        #         n = n/2
        #         if n == 1: 
        #             return True
        #     return False

        # math Logaritmic solution
        if n < 1:
            return False
        import math
        return True if math.log2(n) % 1 == 0 else False        