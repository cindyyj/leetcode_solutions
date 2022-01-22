class Solution:
    # int datatype can use lru_cache while list can not
    @lru_cache()  # this decorator can speed up the program by 30%
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        