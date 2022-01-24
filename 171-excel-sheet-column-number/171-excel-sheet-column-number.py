class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        col = 0
        
        for char in columnTitle:
            # chr() ord()
            digit = ord(char) - ord('A') + 1
            col = col*26 + digit
        
        return col        