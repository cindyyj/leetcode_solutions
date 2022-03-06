class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        s = bin(n)
        return ('00' not in s) and ('11' not in s)
        