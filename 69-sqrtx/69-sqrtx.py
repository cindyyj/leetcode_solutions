class Solution:
    def mySqrt(self, x: int) -> int:
        # newton's method
        r = x
        while r * r > x:
            r = (r + x/r) // 2
        return int(r)
        
#         # cannot use built-in function
#         # pow(x, 0.5) or x**0.5, math.sqrt(x)
        
#         # binary search
        
#         low, high = 0, x
        
#         while low <= high:
#             mid = low + (high - low) // 2
#             if (mid*mid <= x < (mid+1)*(mid+1)):
#                 return mid
#             elif mid*mid > x:
#                 high = mid -1
#             else:
#                 low = mid + 1
#         return low