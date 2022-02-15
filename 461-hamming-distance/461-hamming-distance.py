class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        #  bit operation called XOR which outputs 1 if and only if the input bits are different.
        return bin(x^y).count('1')