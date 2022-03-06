class Solution:
    def sumBase(self, n: int, k: int) -> int:
        
        """
        Time: O(logn), space: O(1).
        Note: O(log(n base k)) = O(logn).
        """
        total = 0
        while n > 0:
            total += n % k
            n //= k
        
        return total