class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        """
        meet the number that can be dived by 5, the Trailing will have 1 more zero.
        meet the number that can be dived by 5*5, the Trailing will have 2 more zero.
        n=25能提供6个5,（因为25这个数就能提供2个5）。
        
        推广:求n!中因子p的个数:
        n! = 1*2*...*n
        所以含有一个p有 n//p
        所以含有一个p*p有 n//p**2
        ... 
        把以上全部加起来即为答案了
        res = n//p + n//p^2 + n//p^3
        
        作者：zeroac
        链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes/solution/c-shu-xue-xiang-xi-tui-dao-by-zeroac/       
        """
        
        fives = 0
        while n > 0:
            n //= 5
            fives += n
        return fives
        
# # --------------------------- METHOD 1  --------------------------- 
#         # Brute Force, TLE, time limit exceed, 0! = 1, 1! = 1
#         if n == 0:
#             return 0 

#         n_factorial = 1
#         for i in range(2, n + 1):
#             n_factorial *= i
            
#         zero = 0
#         while n_factorial % 10 == 0:
#             zero += 1
#             n_factorial //= 10
#         return zero