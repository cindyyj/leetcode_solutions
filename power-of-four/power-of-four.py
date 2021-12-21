class Solution:
    powerlist = [4**i for i in range(31)]
    
    def isPowerOfFour(self, n: int) -> bool:
        return n in Solution.powerlist
        