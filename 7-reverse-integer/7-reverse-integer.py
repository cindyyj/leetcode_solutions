class Solution:
    def reverse(self, x: int) -> int:      
        sign = 1 if x >= 0 else -1
        # sign = [1,-1][x < 0]
        res = sign * int(str(abs(x))[::-1])
        return res if -(2**31)-1 < res < 2**31 else 0

#     def reverse_pos(self, x):    
#         INT_MAX = 2**31 - 1
        
#         rev = 0
#         while x != 0:
#             # go out of range when reversed! 
#             if rev > INT_MAX // 10:
#                 return 0
            
#             x, digit = x // 10, x % 10  # divmod(x, 10)
#             rev = rev*10 + digit
#         return rev
    
    
#     def reverse(self, x: int) -> int:
        
#         if x == 0:
#             return x
#         if x > 0:
#             return self.reverse_pos(x)
#         if x < 0:
#             return -self.reverse_pos(-x)
        

#         # https://leetcode.com/problems/reverse-integer/solution/
#         INT_MIN, INT_MAX = -2**31, 2**31 - 1

#         rev = 0
#         while x != 0:
#             # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
#             if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
#                 return 0
#             digit = x % 10
#             # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
#             if x < 0 and digit > 0:
#                 digit -= 10

#             # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
#             x = (x - digit) // 10
#             rev = rev * 10 + digit
        
#         return rev