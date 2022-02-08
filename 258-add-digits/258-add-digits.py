class Solution:
    def addDigits(self, num: int) -> int:
        
        # one-line (-1 % 9 = 8 in python!!!)
        return 0 if num == 0 else (num - 1) % 9 + 1
        
        # if num == 0:
        #     return 0
        # elif num % 9 == 0:
        #     return 9      
        # else:
        #     return num % 9
        
        
#         digital_root = 0
        
#         while num > 0:
#             digital_root += num % 10 
#             num //= 10
            
#             if num == 0 and digital_root >= 10:
#                 num = digital_root
#                 digital_root = 0
        
#         return digital_root


#         当 num 是 0 时，各位之和是自身 0；
#         当 num 能被 9 整除时，各位之和是 9；
#         当 num 不能被 9 整除时，各位之和是对 9 取余的结果。

#         作者：Dine
#         链接：https://leetcode-cn.com/problems/add-digits/solution/258-ge-wei-xiang-jia-by-dine-s69o/
