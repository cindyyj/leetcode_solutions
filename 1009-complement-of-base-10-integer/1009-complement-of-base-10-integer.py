class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n == 0:
            return 1
        todo, bit = n, 1
        while todo:
            # flip current bit
            n ^= bit
            bit <<= 1
            todo >>= 1
        return n
        