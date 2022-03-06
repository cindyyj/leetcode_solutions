class Solution:
    def findComplement(self, num: int) -> int:
        
        # same as 1009
        # create bitmask of 1111...1 of same length of binary num 
        # bin(1) ->0b1, len(bin(num)) - 2 is the same as bit length
        
        x = '1' * num.bit_length()
        # x = '1'*(len(bin(num)) - 2)          
        return int(x, 2) ^ num # much faster than int(x, 2) - num
        
        # return ((1 << num.bit_length()) - 1) ^ num
    
        """
        def bit_length(self):
            s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
            s = s.lstrip('-0b') # remove leading zeros and minus sign
            return len(s)       # len('100101') --> 6
        """