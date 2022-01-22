class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #  f[i] = min(cost[i] + f[i-1], cost[i] + f[i-2])
        
        n = len(cost)
        
        if n <= 1:
            return 0
        
        dp = [0] * (n + 1)
        
        for i in range(2, n+1):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
        
        return dp[n]