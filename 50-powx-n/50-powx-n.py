from functools import lru_cache

class Solution:
    
    @lru_cache()
    def myPow(self, x: float, n: int) -> float:
        
#         # iterative
#         if n == 0 or x == 1:
#             return 1
#         if x == 0:
#             return 0
        
#         if n < 0:
#             x = 1/x
#             n = -n 
        
#         ans = 1
#         while n > 0:
#             if n & 1: # n % 2 == 1
#                 ans = ans * x
#             n = n >> 1 # n//2
#             x = x*x
#         return ans

        
        # recursive 
        if x == 0: 
            return 0
        if n == 0 or x == 1:
            return 1        
        if n < 0:
            return 1/self.myPow(x, -n)        
        if n % 2:
            return x * self.myPow(x, (n-1))        
        return self.myPow(x*x, n >> 1)  # n // 2

"""
recursive func: 

from functools import lru_cache
@lru_cache()  # lru  least recently used, stored intermediate results, that saves time! 
def fib(n):


> Base Case:  b == 0
> Recursive Function: F(a ^ b) = F( (a*a) ^ b // 2) 

return pow(x, n)


# recursive
# https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed

# 时间复杂度：O(logn)，即为递归的层数。
# 空间复杂度：O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。
Time complexity : O(logn). Each time we apply the formula , n is reduced by half. Thus we need at most O(logn) computations to get the result. - similar to binary search
Space complexity : O(logn). 

python中lru_cache的基本原理是构建一个字典，字典的key为调用参数，value就是该参数的计算结果。

Recursion是什么：
编程角度: Recursion involves a function calling itself.
实际用处:
Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially.
从大化小，知道问题可以小的可以被轻易解决，然后重复同样的步骤直到大问题被解决。
Recursion的意义何在？
更简单理解的业务逻辑
更简短的代码
Recursion的编程实操
Recursion其实大方向就两个步骤：

Base Case:
处理最小的问题：每个Recursion方程都必须有个出口，或者是终止条件。Base Case针对的是Recursion被分解成最小的问题以后，如何解决这个最小问题。所以我们的Base Case一般是做一个我们输入问题是否已经是最小了这么一个对比。每个Recursion必须要有Base Case，避免死循环。
Recursive Function:
把大问题不断变小。
Return:
返回
所以Recursion的口诀就是：这个问题是Base Case么？不是那我们就写Recursion让问题化小，直到变成Base Case，处理并且返回

https://github.com/yuzhoujr/leetcode/issues/43

"""