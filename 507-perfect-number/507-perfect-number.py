class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
        # 它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。 1不算在内
        
        if num <= 1:
            return False
        
        total = 1
        d = 2
        while d * d <= num:
            if num % d == 0:
                total += d + num // d
            d += 1
        
        if int(num**0.5) ** 2 == num:
            total -= int(num**0.5) 
        
        return total == num