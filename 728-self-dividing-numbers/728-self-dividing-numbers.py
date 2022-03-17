class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def selfdivide(num):           
            digits = list(map(int, str(num)))
            for d in digits:
                if d == 0 or num % d != 0:
                    return False
            return True
        
        return [i for i in range(left, right + 1) if selfdivide(i)]