import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        # gcd Euclidean algorithm (辗转相除法)
        # 对于两个非负整数 x, y , (x > y), gcd(x, y) = gcd(y, x mod y)
        
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)
        
        return gcd(max(nums), min(nums))
        
        
        
        # return math.gcd(min(nums), max(nums))
        
        
        