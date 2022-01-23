class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # https://leetcode.com/problems/sum-of-square-numbers/solution/
        # 5 solutions, include using Fermat Theorem (too complicated)
        # n**2 = 1+3+..+ (2n-1) = 2*(1+2+3+...+n) -n = 2*n(n+1)/2 - n = n**2
        
        # sqrt
        for a in range(int(c**0.5)+1):
            b = (c - a*a)**0.5
            if b == int(b):
                return True
        return False
        
#         # Hashset
#         # https://leetcode.com/problems/sum-of-square-numbers/discuss/1424957/Python-3-solutions%3A-Sqrt-HashSet-Two-Pointers-Clean-and-Concise-O(sqrt(c)) 
#         # transforms this into two sum
#         # Complexity
#         # Time: O(sqrt(c)), where c <= 2^31-1
#         # Space: O(sqrt(c))
        
#         squares = set()
#         for i in range(int(c**0.5)+1):
#             squares.add(i*i)
            
#         for a_square in squares:
#             b_square = c - a_square
#             if b_square in squares:
#                 return True
        
#         return False

        
#         # two pointer
#         # https://leetcode-cn.com/problems/sum-of-square-numbers/solution/shuang-zhi-zhen-de-ben-zhi-er-wei-ju-zhe-ebn3/
#         # becomes search in a 2d matrix
#         # Complexity
#         # Time: O(sqrt(c)), where c <= 2^31-1
#         # Space: O(1)
            
#         low, high = 0, int(c**0.5)
        
#         while low <= high:
#             s = low*low + high*high

#             if s == c:
#                 return True
#             if s < c:
#                 low += 1
#             else:
#                 high -= 1
        
#         return False                