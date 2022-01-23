class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # https://leetcode.com/problems/sum-of-square-numbers/solution/
        # 5 solutions, include using Fermat Theorem (too complicated)
        # n**2 = 1+3+..+ (2n-1) = 2*(1+2+3+...+n) -n = 2*n(n+1)/2 - n = n**2
        
        # two pointer
        # https://leetcode-cn.com/problems/sum-of-square-numbers/solution/shuang-zhi-zhen-de-ben-zhi-er-wei-ju-zhe-ebn3/
        # becomes search in a 2d matrix
        
        low, high = 0, int(c**0.5)
        
        while low <= high:
            s = low*low + high*high

            if s == c:
                return True
            if s < c:
                low += 1
            else:
                high -= 1
        
        return False                