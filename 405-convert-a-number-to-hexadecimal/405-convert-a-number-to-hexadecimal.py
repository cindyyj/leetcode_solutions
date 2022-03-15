class Solution:
    def toHex(self, num: int) -> str:
        
        s, res = '0123456789abcdef', ''
        
        # two’s complement
        if num < 0:
            num += 2**32
            
        # no need to reverse, otherwise, res += s[num % 16], return res[::-1]            
        while num:
            res = s[num % 16] + res 
            num >>= 4
        
        return res or '0'