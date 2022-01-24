class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        title = ""
        while columnNumber:
            # chr() char <-> ord() int
            # ord() function takes string argument of a single Unicode character and return its integer Unicode code point value
            # chr() function takes integer argument and return the string representing a character at that code point.

            columnNumber, remainder = divmod(columnNumber - 1, 26)
            title += chr(remainder + ord('A'))
            
        return title[::-1]