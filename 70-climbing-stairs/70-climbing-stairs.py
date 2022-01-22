class Solution:
    # int datatype can use lru_cache while list can not
    @lru_cache()  # this decorator can speed up the program by 30%
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        
        for i in range(n+1):
            if i <= 2:
                dp[i] = i
            else:
                dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
#         if n <= 2:
#             return n
        
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
        