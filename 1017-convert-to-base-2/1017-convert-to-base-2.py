class Solution:
    def baseNeg2(self, n: int) -> str:
        
        """
        In base 2 we multiply bits to 1, 2, 4, 8 ... to get actual number in decimal. 
        So for base -2, we need to multiply bits with 1, -2, 4, -8 ... to get number in decimal. 
        Therefore, we can use -(N >> 1) or just change the negative remainder to positive 
        wiki, https://en.wikipedia.org/wiki/Negative_base#Calculation
        "Note that in most programming languages, 
        the result (in integer arithmetic) of dividing a negative number by a negative number is rounded towards 0, 
        usually leaving a negative remainder.... 
        in such case, computer implementations of the above algorithm should add 1 and r to the quotient and remainder respectively."-
        """
        if n == 0:
            digits = ['0']
        else:
            digits = []
            while n != 0:
                n, remainder = divmod(n, -2)
                if remainder < 0:
                    n, remainder = n + 1, remainder + 2
                digits.append(str(remainder))
        return "".join(digits[::-1])
        
        
        # if n == 0:
        #     return '0'     
        # res = []
        # while n:
        #     res.append(n & 1)
        #     n = -(n >> 1)
        # return "".join(map(str, res[::-1]))
        
        
        