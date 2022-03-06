class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bit_count(num):
            if num == 0:
                return 0
            
            bits = 0
            while num > 0:
                if num % 2 == 1:
                    bits += 1
                num //= 2
            
            return bits
        
        return sorted(arr, key=lambda x: (bit_count(x), x))
        
        # return sorted(arr, key=lambda x: (bin(x).count('1'), x))
        