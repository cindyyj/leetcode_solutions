import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # 链接：https://leetcode-cn.com/problems/find-greatest-common-divisor-of-array/solution/zhan-zhuan-xiang-chu-fa-geng-xiang-jian-mu306/
        # 更相减损术，出自《九章算术》（原本是为了求约分，修改后可用来求解最大公约数）的一种求最大公约数的算法。
        # 其基本思路为（搬运自百度百科）：以较大的数减较小的数，接着把所得的差与较小的数比较，并以大数减小数。继续上述操作，直到所得的减数和差相等为止。
        
        def gcd(x, y):
            if x == y:
                return x
            elif x < y:
                return gcd(y - x, x)
            return gcd(x - y, y)
        return gcd(max(nums), min(nums))
        
        
        
        
        # # gcd Euclidean algorithm (辗转相除法)
        # # 对于两个非负整数 x, y , (x > y), gcd(x, y) = gcd(y, x mod y)        
        # def gcd(x, y):
        #     if x <= y:
        #         return gcd(y, x)
        #     if y == 0:
        #         return x
        #     return gcd(y, x % y)        
        # return gcd(max(nums), min(nums))
        
        
        
        # return math.gcd(min(nums), max(nums))
        
        
        