class Solution:
    def myPow(self, x: float, n: int) -> float:
        # pos
        # n odd, x**n = x*(x**2)**(n-1)/2
        # n even, x**n = (x**2)**n/2
        # x is called the base, and the number n is called the exponent.
        # 0
        # neg
        
        # recursive
        # https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
        
        if n == 0:
            return 1
        
        if n < 0:
            return 1/self.myPow(x, -n)
        
        if n % 2:
            return x * self.myPow(x, (n-1))
        
        return self.myPow(x*x, n/2)