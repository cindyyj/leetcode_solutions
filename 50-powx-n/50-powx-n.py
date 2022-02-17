from functools import lru_cache

class Solution:
    
    @lru_cache()
    def myPow(self, x: float, n: int) -> float:
        
        # recursive 
        if n == 0:
            return 1        
        if n < 0:
            return 1/self.myPow(x, -n)        
        if n % 2:
            return x * self.myPow(x, (n-1))        
        return self.myPow(x*x, n/2)

"""
> Base Case:  b == 0
> Function: F(a ^ b) = F( (a*a) ^ b // 2) 

return pow(x, n)
# pos
# n odd, x**n = x*(x**2)**(n-1)/2
# n even, x**n = (x**2)**n/2
# x is called the base, and the number n is called the exponent.
# 0
# neg

# recursive
# https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed

# 时间复杂度：O(logn)，即为递归的层数。
# 空间复杂度：O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。
Time complexity : O(logn). Each time we apply the formula , n is reduced by half. Thus we need at most O(logn) computations to get the result. - similar to binary search
Space complexity : O(logn). 

python中lru_cache的基本原理是构建一个字典，字典的key为调用参数，value就是该参数的计算结果。

"""