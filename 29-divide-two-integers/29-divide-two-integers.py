class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1 # multiply by 2 with bit operations
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2**31, res), 2**31 - 1)

#     # official, exceeds time
#         # Constants.
#         MAX_INT = 2147483647        # 2**31 - 1
#         MIN_INT = -2147483648       # -2**31

#         # Special case: overflow.
#         if dividend == MIN_INT and divisor == -1:
#             return MAX_INT

#         # We need to convert both numbers to negatives
#         # for the reasons explained above.
#         # Also, we count the number of negatives signs.
#         negatives = 2
#         if dividend > 0:
#             negatives -= 1
#             dividend = -dividend
#         if divisor > 0:
#             negatives -= 1
#             divisor = -divisor

#         # Count how many times the divisor has to be
#         # added to get the dividend. This is the quotient.
#         quotient = 0
#         while dividend - divisor <= 0:
#             quotient -= 1
#             dividend -= divisor

#         # If there was originally one negative sign, then
#         # the quotient remains negative. Otherwise, switch
#         # it to positive.
#         return -quotient if negatives != 1 else quotient   
