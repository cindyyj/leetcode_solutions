class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        d = 0
        
        # method 1: remove the rightmost bit of '1'
        while xor:
            d += 1
            xor = xor & (xor - 1)        
        
        # method 2: rightmost bit is 1 or not
        # while xor:
        #     if xor & 1:
        #         d += 1
        #     xor = xor >> 1
        
        return d
    
        
        #  bit operation called XOR which outputs 1 if and only if the input bits are different.
        return bin(x^y).count('1')
    
    
    """
    bitwise operation
    - rightmost bit: check if the rightmost bit is one, which we can use either the modulo operation (i.e. i % 2) or the bit AND operation (i.e. i & 1). Both operations would mask out the rest of the bits other than the rightmost bit.
    - logical shift: 
    """