class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        s = ""
        for c in word:
            if c.isdigit():
                s += c
            else:
                s += " "
        
        # s = "".join(c if c.isdigit() else ' ' for c in word)
        return len(set(map(int, s.split())))