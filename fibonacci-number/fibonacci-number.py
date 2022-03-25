class Solution:
    def fib(self, n: int) -> int:

        # dp
        
        if n < 2:
            return n
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
#         # SOLUTION 1: this is an iterative solution that is efficient
#         if n < 2:
#             return n
#         a = 0
#         b = 1
#         for i in range(2, n + 1):
#             a, b = b, a + b
#         return b
    
#         # SOLUTION 2: this is a solution that uses dynamic programming
#         # dp = [i for i in range(n + 1)]
#         # for i in range(2, n + 1):
#         #     dp[i] = dp[i - 1] + dp[i - 2]
#         # return dp[n]
        
#         # SOLUTION 3: this is a recursive soltion that is inefficient, but is easy to understand if you struggle with recursion
#         # if n < 2:
#         #     return n
#         # else:
#         #     return self.fib(n - 1) + self.fib(n - 2)