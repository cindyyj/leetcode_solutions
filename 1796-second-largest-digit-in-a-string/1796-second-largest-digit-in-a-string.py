class Solution:
    def secondHighest(self, s: str) -> int:
        
        # https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python/44891278
        # Bascially, str.isdigit only returns True for what I said before, strings containing solely the digits 0-9.

        # By contrast, str.isnumeric returns True if it contains any numeric characters. 
        # When I first read this, I figured that it would mean decimal points and minus signs — but no! 
        # It’s just the digits 0-9, plus any character from another language that’s used in place of digits.
        
        digits = [int(c) for c in s if c.isdigit()]
        
        if not digits:
            return -1 
        
        digits.sort(reverse = True)
        
        # in case multiple copy of largest number
        # alternatively can sort set(digits)
        for v in digits:
            if v!= digits[0]:
                return v 
        
        return -1