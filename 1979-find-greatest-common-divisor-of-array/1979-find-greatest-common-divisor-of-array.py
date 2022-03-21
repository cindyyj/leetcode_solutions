import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # 方法三：Stein算法
        # Stein算法 是一种计算两个数最大公约数的算法，是针对欧几里得算法在对大整数进行运算时，需要试商导致增加运算时间的缺陷而提出的改进算法。

        # 其基本思路为：

        # 对于给定的两个正整数 x, yx,y，判断它们是否都是偶数：若是，则用2约简，直至两者不同时为偶数。
        # 将两数中的偶数（如存在）进一步约简为奇数；以较大的数减较小的数，接着把所得的差与较小的数比较，并以大数减小数。
        # 继续上述第2步操作，直到所得的减数和差相等为止。
        # 最终，第1步中约掉的若干个2的积与第3步中等数的乘积就是所求的最大公约数。
        
        def gcd(x, y):
            if x < y: # ensure x > y
                x, y = y, x
            
            if y == 0:
                return x
            
            if x % 2 == y % 2 == 0:
                return 2*gcd(x//2, y//2)
            if x % 2 == 0:
                return gcd(x//2, y)
            if y % 2 == 0:
                return gcd(x, y//2)
            # for both odds
            return gcd((x-y)//2, y)
        
        return gcd(max(nums), min(nums))
        
        
        
        # 链接：https://leetcode-cn.com/problems/find-greatest-common-divisor-of-array/solution/zhan-zhuan-xiang-chu-fa-geng-xiang-jian-mu306/
#         # 更相减损术，出自《九章算术》（原本是为了求约分，修改后可用来求解最大公约数）的一种求最大公约数的算法。
#         # 其基本思路为（搬运自百度百科）：以较大的数减较小的数，接着把所得的差与较小的数比较，并以大数减小数。继续上述操作，直到所得的减数和差相等为止。
        
#         def gcd(x, y):
#             if x == y:
#                 return x
#             elif x < y:
#                 return gcd(y - x, x)
#             return gcd(x - y, y)
#         return gcd(max(nums), min(nums))

        
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
        
        
        