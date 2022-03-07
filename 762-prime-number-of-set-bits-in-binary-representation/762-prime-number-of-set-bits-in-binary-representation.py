class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # len(bin(10**6))-2 = 20, int(math.log2(10**6)) + 1
        # binary representation should be less or equal to 20 digits
        
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        
        target = 0
        for p in primes:
            target += 1 << p  # set only prime position bits
            
        return sum( (target >> bin(i).count('1')) & 1 for i in range(left, right + 1))