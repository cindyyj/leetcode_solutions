class Solution:
    def isThree(self, n: int) -> bool:
        # 穷举: 三除数的必须条件是质数的平方。并且N<10000,穷举100以内的质数的平方即可。
        if n == 1: # edge case
            return False

        sqrt = int(n**.5)
        return sqrt*sqrt == n and all(n%a for a in range(2, sqrt))