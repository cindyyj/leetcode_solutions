class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

#         # The integer-array "digits" is first converted into a joined string: [1,2,3] -> "123". Code: a = ''.join(map(str,digits))
#         # The joined string is then converted into an integer, and we add one. *Code: b = int(a)+1
#         # Our new integer is re-converted into a string, and then into a list format. 
#         # Finally, the INT operator is applied to each element of the list to obtain new integer digits 
#         # *Code: [ int(c) for c in str(b) ] or list(map(int,str(b)))
#         return [int(x) for x in str( int(''.join(map(str, digits)))+1 )]
        
        # Hard-Working Version: Manual Digit Check
        # O(1) space, and O(1) time for most cases as well (with few chained 9's in the lower digits)        
        if not digits:
            return digits
        
        i = len(digits) -1
        digits[i] += 1
        
        while digits[i] == 10:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
            else:
                digits[i-1] += 1
                i -= 1
        
        return digits