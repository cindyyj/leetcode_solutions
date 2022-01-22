class Solution:
    # int datatype can use lru_cache while list can not
    
    # Fibonacci relation has a characteristic equation s**2−s−1=0    
    @lru_cache()  # this decorator can speed up the program by 30%
    
    def climbStairs(self, n: int) -> int:
        # exactly same as Fib
        # https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
        # Rolling array is a programming idea in DP. 
        
        if n <= 2:
            return n
        
        left = 0
        mid = 1
        right = 2
        
        for i in range(3, n + 1):
            left = mid
            mid = right
            right = left + mid
        
        return right

#         # dp
#         dp = [0] * (n + 1)
        
#         for i in range(n+1):
#             if i <= 2:
#                 dp[i] = i
#             else:
#                 dp[i] = dp[i-1] + dp[i-2]
        
#         return dp[n]
        
#         # # recursion
#         # needs @lru_cache() Least Recently Used to speed up, otherwise exceed time limit
#         if n <= 2:
#             return n
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
        