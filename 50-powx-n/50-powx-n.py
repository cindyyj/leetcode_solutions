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
        
        # 时间复杂度：O(logn)，即为递归的层数。
        # 空间复杂度：O(\log n)O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。

        if n == 0:
            return 1
        
        if n < 0:
            return 1/self.myPow(x, -n)
        
        if n % 2:
            return x * self.myPow(x, (n-1))
        
        return self.myPow(x*x, n/2)