class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        f1, f2 = [], []
        for x in range(1, int(n**0.5) + 1):
            if n % x == 0:
                f1.append(x)
                f2.append(n // x)
            
        # in case n is perfect square
        if f1[-1] == f2[-1]:
            f2.pop()
        
        factors = f1 + f2[::-1]
        return -1 if len(factors) < k else factors[k-1]
        
        
#         # brute force
#         for x in range(1, n//2 + 1):
#             if n % x == 0:
#                 k -= 1
#                 if k == 0:
#                     return x
        
#         return n if k == 1 else -1
        