class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            x_reverse = - int(str(abs(x))[::-1])
            if x_reverse < -2**31:
                return 0
 
        else:
            x_reverse = int(str(x)[::-1])
            if x_reverse > (2**31-1):
                return 0
            
        return x_reverse