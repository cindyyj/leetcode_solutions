class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Newton's method
        r = num
        while r*r > num:
            r = (r + num/r) // 2
        return r*r == num
        
        
#         # Binary Search
#         if num <= 0: return False
        
#         l, r = 1, num
        
#         while l <= r:
#             mid = l + (r - l) // 2
#             if mid * mid == num:
#                 return True
#             elif mid * mid < num < (mid + 1)*(mid + 1):
#                 return False
#             elif mid * mid > num:
#                 r = mid - 1
#             else:
#                 l = mid + 1
        
#         return False
        
        
#         # https://leetcode.com/problems/valid-perfect-square/discuss/130010/Python-4-Methods-with-time-testing
# # Solving with Bitwise trick.
#     def BitwiseTrick(self, num):
#         root = 0
#         bit = 1 << 15

#         while bit > 0 :
#             root |= bit
#             if root > num // root:    
#                 root ^= bit                
#             bit >>= 1        
#         return root * root == num
    
# # Using Newton's Method
#     def NewtonMethod(self, num):
#         r = num
#         while r*r > num:
#             r = (r + num/r) // 2
#         return r*r == num
    
# # Math Trick for Square number is 1+3+5+ ... +(2n-1)
#     def Math(self, num):
#         i = 1
#         while (num>0):
#             num -= i
#             i += 2       
#         return num == 0
    
# # Binary Search Method
#     def BinarySearch(self, num):
#         left = 0
#         right = num
        
#         while left <= right:
#             mid = left + (right-left)//2
#             if  mid ** 2 == num:
#                 return True
#             elif mid ** 2 > num:
#                 right = mid -1
#             else:
#                 left = mid +1
#         return False
    
# # Linear Method (Naive) - For comparison
#     def Linear(self, num):
#         i = 1
#         while i ** 2 <= num:
#             if i ** 2 == num:
#                 return True
#             else:
#                 i += 1
#         return False
    
# #         I test these five methods with for i in range(100000): function(i), and get results as below.

# #         Time for Bitwise's Method : 0.45249104499816895
# #         Time for Newton's Method : 0.3492701053619385 BEST!!!
# #         Time for Math's Method : 2.641957998275757
# #         Time for Binary Search's Method : 1.5031492710113525
# #         Time for Linear's Method : 17.613927125930786