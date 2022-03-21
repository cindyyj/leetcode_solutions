class Solution:
    def isThree(self, n: int) -> bool:
        # 穷举: 三除数的必须条件是质数的平方。并且N<10000,穷举100以内的质数的平方即可。
        
        primes = set([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])
        sqrt = math.sqrt(n)
        if sqrt in primes:
            return True
        else:
            return False
        
        # if n == 1: # edge case
        #     return False
        # sqrt = int(n**.5)
        # return sqrt*sqrt == n and all(n%a for a in range(2, sqrt))