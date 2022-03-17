class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        # https://leetcode.com/problems/self-dividing-numbers/discuss/162578/One-line-Python-(Learn-some-Python-tricks-that-you-might-not-know)
        # to do: many optimization tricks to read
        
        def selfdivide(num):           
            digits = list(map(int, str(num)))
            for d in digits:
                if d == 0 or num % d != 0:
                    return False
            return True
        
        return [i for i in range(left, right + 1) if selfdivide(i)]