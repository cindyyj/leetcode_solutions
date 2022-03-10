class Solution:
    def countTriples(self, n: int) -> int:
        # brute force
        
        res = 0
        
        # no need to loop a, b til n 
        # n**2 + n**2 > n**2 
        
        # here forces a < b; if (3, 4, 5) is valid, then (4, 3, 5) is also valid
        # res += 2
        
        for a in range(1, n):
            for b in range(a + 1, n):
                c = (a * a + b * b) ** 0.5
                if int(c) == c and c <= n:
                    res += 2
        
        return res