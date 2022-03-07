class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # s = bin(n)
        # return ('00' not in s) and ('11' not in s)
        
        # n, cur_digit = divmod(n, 2)
        # while n > 0:
        #     if cur_digit == n % 2:
        #         return False
        #     n, cur_digit = divmod(n, 2)
        # return True
        
        bits = bin(n)
        return all( bits[i] != bits[i+1] for i in range(len(bits) - 1))