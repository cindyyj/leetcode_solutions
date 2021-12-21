class Solution:    
#     BIG = 3**19
    
#     def isPowerOfThree(self, n: int) -> bool:    
#         # method 2: divisor of 3 power 19
#         return (n > 0) and (Solution.BIG % n == 0)        

    def isPowerOfThree(self, n: int) -> bool:   
        while n and (n % 3 == 0):
            n /= 3
        
        return n == 1         
